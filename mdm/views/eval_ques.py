from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import render
from rest_framework.response import Response

from management.models import CommCd
from management.serializers import CommCdSerializer
from mdm.models import EvalItem, AbltQuesPool
from mdm.serializers import EvalItemSerializer, QuesPoolSerializer, CreateQuesPoolSerializer


# 역량평가대분류코드
eval_item_clss = CommCd.objects.filter(hi_comm_cd='CC013000')
eval_item_clss_serializer = CommCdSerializer(eval_item_clss, many=True)

# 답변유형코드
ans_type_list = CommCd.objects.filter(hi_comm_cd='CC012000')
ans_type_list_serializer = CommCdSerializer(ans_type_list, many=True)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_all_question(request, **kwargs):
    eval_item_list = EvalItem.objects.all()
    eval_item_list_serializer = EvalItemSerializer(eval_item_list, many=True)

    ablt_ques_pool = AbltQuesPool.objects.filter(del_yn='N')
    ablt_ques_pool_serializer = QuesPoolSerializer(ablt_ques_pool, many=True)

    return render(request, 'eval_ques/eval_ques.html',
                  {'eval_item_clss': eval_item_clss_serializer.data,
                   'eval_item_list': eval_item_list_serializer.data,
                   'ans_type_list': ans_type_list_serializer.data,
                   'ablt_ques_pool': ablt_ques_pool_serializer.data,
                   **kwargs})


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def save_question(requests):
    req = requests.data
    try:
        ques_dict = {
            "eval_item_no": int(req["eval_item_no"]),
            "question": req["question"],
            "rslt_msr_type": req["rslt_msr_type"],
            "ans_type": req["ans_type"],
            "reg_mem_no": requests.user.id,
            "modf_mem_no": requests.user.id
        }
        # if: 평가문항 저장 / else: 평가문항 수정
        if req["ablt_ques_no"] == "":
            serializer = CreateQuesPoolSerializer(data=ques_dict)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(
                    {"status": status.HTTP_201_CREATED}
                )
        else:
            ablt_ques_no = int(req["ablt_ques_no"])
            update_question = AbltQuesPool.objects.get(ablt_ques_no=ablt_ques_no)
            serializer = CreateQuesPoolSerializer(update_question, data=ques_dict)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(
                    {"status": status.HTTP_200_OK}
                )

    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_question(request):
    if request.method == 'GET':
        ablt_ques_no = int(request.GET['ablt_ques_no'])
        selected_question = AbltQuesPool.objects.get(ablt_ques_no=ablt_ques_no)
        question_serializer = QuesPoolSerializer(selected_question)

        eval_item_list = EvalItem.objects.filter(eval_item_clss=selected_question.eval_item_no.eval_item_clss)
        eval_item_list_serializer = EvalItemSerializer(eval_item_list, many=True)

        return render(request, 'eval_ques/eval_ques_detail.html',
                      {'ablt_ques': question_serializer.data,
                       'eval_item_clss': eval_item_clss_serializer.data,
                       'eval_item_list': eval_item_list_serializer.data,
                       'ans_type_list': ans_type_list_serializer.data})

    if request.method == 'DELETE':
        try:
            ablt_ques_no = request.data['ablt_ques_no']
            question = AbltQuesPool.objects.get(ablt_ques_no=ablt_ques_no)
            question.del_yn = 'Y'
            question.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def ajax_add_question(request):
    eval_item_list = EvalItem.objects.all()
    eval_item_list_serializer = EvalItemSerializer(eval_item_list, many=True)

    return render(request, 'eval_ques/eval_ques_detail.html',
                  {'eval_item_clss': eval_item_clss_serializer.data,
                   'ans_type_list': ans_type_list_serializer.data,
                   'eval_item_list': eval_item_list_serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def ajax_get_eval_item(request):
    cd_nm = request.GET['cd_nm']
    item_clss = CommCd.objects.get(cd_nm=cd_nm)

    eval_item_list = EvalItem.objects.filter(eval_item_clss=item_clss.comm_cd)
    eval_item_list_serializer = EvalItemSerializer(eval_item_list, many=True)

    return render(request, 'eval_ques/eval_item_select_box.html',
                  {"eval_item_list": eval_item_list_serializer.data})
