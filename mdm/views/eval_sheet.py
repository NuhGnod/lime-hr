import time

from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse, QueryDict
from rest_framework.response import Response

from config.utils import dict_fetchall
from management.models import CommCd
from management.serializers import CommCdSerializer
from mdm.models import EvalSheet, AbltEvalQues, AbltQuesPool, AbltEvalRslt
from mdm.serializers import EvalSheetSerializer, joinSerializer, AbltEvalQuesSerializer


# 평가지 view


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([AllowAny])
def sheet(request, *args, **kwargs):
    reqdata = request.data.copy()
    reqdata['modf_mem_no'] = request.user.id
    if request.method == 'GET':
        eval_sheet_no = request.GET.get('eval_sheet_no')
        data = {
            'sheet_nm': ""
        }

        objects_all = EvalSheet.objects.filter(del_yn='N')  # 평가지 데이터 리스트
        eval_sheet_serializer = EvalSheetSerializer(objects_all, many=True)

        objects_filter = CommCd.objects.filter(hi_comm_cd="CC010000")  # 평가 구분 코드
        eval_clss_list = CommCdSerializer(objects_filter, many=True)

        if eval_sheet_no is not None:  # 왼쪽의 리스트에서 row 하나 클릭한 상태.
            get = EvalSheet.objects.filter(eval_sheet_no=eval_sheet_no)  # 해당 row의 pk로 데이터 가져옴.
            ques_objects_filter = AbltEvalQues.objects.filter(eval_sheet_no=eval_sheet_no, del_yn='N')
            ques_serializer = AbltEvalQuesSerializer(ques_objects_filter, many=True)  # 중첩 serializer
            eval_ques_able = True
            serializer = EvalSheetSerializer(get, many=True)
            data = serializer.data
            return render(request, 'eval_sheet/eval_sheet_detail.html', {'eval_sheet': data,
                                                                         'eval_clss_list': eval_clss_list.data,
                                                                         'ablt_ques_no_list': ques_serializer.data,
                                                                         'eval_ques_able': eval_ques_able
                , **kwargs})
        eval_ques_able = False

        return render(request, 'eval_sheet/eval_sheet.html',
                      {'eval_sheet_list': eval_sheet_serializer.data,
                       'eval_clss_list': eval_clss_list.data,
                       'eval_sheet': data,
                       'eval_ques_able': eval_ques_able,
                       **kwargs})

    if (request.method == 'POST'):
        # 평가지 저장 로직

        reqdata['reg_mem_no'] = request.user.id

        if int(reqdata['origin_eval_sheet_no']) < 1:
            # 새로운 평가지가 생성되어야 하는 경우.

            # 평가지 저장
            sheet_serializer = EvalSheetSerializer(data=reqdata, partial=True)
            sheet_serializer.is_valid()
            sheet_serializer.save()

        else:
            # 평가지 설문 결과 테이블을 참조하여 관련된 데이터가 존재할 시, 수정 불가
            rslt_objects_filter = AbltEvalRslt.objects.filter(eval_sheet_no=reqdata['origin_eval_sheet_no'])
            if len(rslt_objects_filter) > 0:
                return JsonResponse({"status": status.HTTP_405_METHOD_NOT_ALLOWED,
                                     })

            # 기존에 존재하는 평가지에서 저장버튼이 눌린 경우.
            # 무언가 수정되는 로직이다.

            to_string = render_to_string('sql/sheet/upsert_eval_sheet.sql',
                                         {"eval_sheet_no": reqdata['origin_eval_sheet_no'],
                                          "eval_clss": reqdata['eval_clss'], "sheet_nm": reqdata['sheet_nm'],
                                          "sheet_desc": reqdata['sheet_desc'], "reg_mem_no": reqdata['reg_mem_no'],
                                          "modf_mem_no": reqdata['modf_mem_no']})

            l = dict_fetchall(to_string)

            for i in range(len(request.data) - 4):
                # 이 반복 횟수는 ablt_ques_no의 갯수(즉 항목추가된 갯수)이다.
                print((reqdata))
                string = render_to_string('sql/sheet/upsert_ablt_eval_ques.sql',
                                          {"eval_sheet_no": reqdata['origin_eval_sheet_no'],
                                           "ablt_ques_no": int(reqdata.getlist('ablt_ques_no[{}][]'.format(i))[0]),
                                           "eval_trgt_clss": reqdata.getlist('ablt_ques_no[{}][]'.format(i))[1],
                                           "otpt_order": int(reqdata.getlist('ablt_ques_no[{}][]'.format(i))[2]),
                                           "reg_mem_no": reqdata.get('reg_mem_no'),
                                           "modf_mem_no": reqdata.get('modf_mem_no')})
                fetchall = dict_fetchall(string)

        return JsonResponse({
            "status" : status.HTTP_200_OK
        })

    if request.method == 'DELETE':
        # 평가지 삭제 로직

        # 평가지 설문 결과 테이블을 참조하여 관련된 데이터가 존재할 시, 삭제 불가

        rslt_objects_filter = AbltEvalRslt.objects.filter(eval_sheet_no=reqdata['eval_sheet_no'])
        if len(rslt_objects_filter) > 0:
            return JsonResponse({"status": status.HTTP_405_METHOD_NOT_ALLOWED,
                                 })

        reqdata['eval_sheet_no'] = int(request.data.get('eval_sheet_no'))
        q = EvalSheet.objects.filter(eval_sheet_no=int(request.data.get('eval_sheet_no'))).first()
        serializer1 = EvalSheetSerializer(q, data=reqdata, partial=True)
        serializer1.is_valid()
        serializer1.save()
        return JsonResponse({"status": status.HTTP_204_NO_CONTENT,
                             })


@api_view(['GET'])
@permission_classes([AllowAny])
def modal(req):
    if (req.method == 'GET'):
        related = AbltQuesPool.objects.all()
        serializers = joinSerializer(related, many=True)

        return render(req, 'eval_sheet/eval_ques_pool_list.html', {'full_data': serializers.data})


@api_view(['DELETE'])
@permission_classes([AllowAny])
def eval_ques_delete(req):
    # 평가지상의 평가항목 삭제 로직
    reqdata = req.data.copy()
    # 이미 평가된 평가지상의 평가항목을 삭제하려는 경우, 삭제 불가.
    rslt_objects_filter = AbltEvalRslt.objects.filter(eval_sheet_no=reqdata['eval_sheet_no'])
    if len(rslt_objects_filter) > 0:
        return JsonResponse({"status": status.HTTP_405_METHOD_NOT_ALLOWED,
                             })

    reqdata['eval_sheet_no'] = int(reqdata.get('eval_sheet_no'))
    reqdata['ablt_ques_no'] = int(reqdata.get('ablt_ques_no'))

    reqdata['modf_mem_no'] = req.user.id

    eval_ques_sql = render_to_string('sql/sheet/update_eval_ques.sql',
                                     {"modf_mem_no": reqdata['modf_mem_no'],
                                      "del_yn": 'Y',
                                      "eval_sheet_no": reqdata['eval_sheet_no'],
                                      "ablt_ques_no": reqdata['ablt_ques_no'],
                                      "eval_trgt_clss": reqdata['eval_trgt_clss']
                                      })
    eval_ques = dict_fetchall(eval_ques_sql)

    return JsonResponse({"status": status.HTTP_204_NO_CONTENT,
                         })


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def create_eval_sheet(req):
    empty_eval_sheet = {
        "eval_sheet_nm": ""
    }
    objects_filter = CommCd.objects.filter(hi_comm_cd="CC010000")  # 평가 구분 코드
    eval_clss_list = CommCdSerializer(objects_filter, many=True)
    return render(req, 'eval_sheet/eval_sheet_detail.html',
                  {'eval_sheet': empty_eval_sheet, 'eval_clss_list': eval_clss_list.data, })


@api_view(['GET'])
@permission_classes([AllowAny])
def ajax_sample(request):
    print(request.GET.get('value'))
    result = dict(test="ssssssss")
    return JsonResponse(result)
