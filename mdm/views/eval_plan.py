from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render, redirect
from django.urls import reverse

from management.models import CommCd
from mdm.models import EvalPlan, EvalSheet, AbltEvalRslt
from mdm.serializers import (
    GetEvalPlanSerializer, GetEvalPlanDetailSerializer, GetEvalSheetSerializer, CreateEvalPlanSerializer, DelEvalPlanSerializer
    )
from management.serializers import CommCdMapperSerializer
# 평가지 view


# 모든 평가계획 리스트 반환
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_evaluation_plan(request, *args, **kwargs):

    eval_plan_qs = EvalPlan.objects.filter(del_yn="N").order_by("-eval_strt_dt")
    eval_plan_serializer = GetEvalPlanSerializer(eval_plan_qs, many=True)

    return render(request, 'eval_plan/eval_plan.html', {"eval_plan_ls": eval_plan_serializer.data})


# 평가 계획 상세
@api_view(['POST', "GET"])
@permission_classes([AllowAny])
def get_detail_eval_plan(request):
    req = request.data.copy()

    # 평가지 목록 가져오기
    eval_sheet_qs = EvalSheet.objects.filter(del_yn='N')
    eval_sheet_serializer = GetEvalSheetSerializer(eval_sheet_qs, many=True)

    # 평가 구분 목록 가져오기
    eval_clss_qs = CommCd.objects.filter(hi_comm_cd='CC010000', del_yn='N').exclude(comm_cd="CC010003")
    eval_clss_serializer = CommCdMapperSerializer(eval_clss_qs, many=True)

    # 평가 계획 상세 반환
    if request.method == "POST":
        plan_no = req['plan_no']

        # 평가 계획 상세 가져오기
        eval_plan_qs = EvalPlan.objects.filter(eval_plan_no=plan_no, del_yn='N').first()
        eval_plan_serializer = GetEvalPlanDetailSerializer(eval_plan_qs)
        return render(request, 'eval_plan/eval_plan_detail.html', {'eval_sheet_ls': eval_sheet_serializer.data,
                                                                   'eval_plan_detail': eval_plan_serializer.data,
                                                                   'eval_clss_ls': eval_clss_serializer.data
                                                                   })
    # 평가 계획 작성 폼 반환
    if request.method == "GET":
        # 기본 날짜 정보 전달
        eval_plan_detail = {
            "eval_strt_dt": datetime.now().strftime("%m/%d/%Y"),
            "eval_end_dt": datetime.now().strftime("%m/%d/%Y"),
        }
        return render(request, 'eval_plan/eval_plan_detail.html', {'eval_sheet_ls': eval_sheet_serializer.data,
                                                                   'eval_plan_detail': eval_plan_detail,
                                                                   'eval_clss_ls': eval_clss_serializer.data
                                                                   })


# 평가 계획 생성 및 수정
@api_view(['POST'])
@permission_classes([AllowAny])
def save_eval_plan(request):
    req = request.data
    print(req)

    date_range = [date.strip() for date in req['date_range'].split('-')]
    eval_strt_dt = datetime.strptime(date_range[0], '%m/%d/%Y').strftime("%Y-%m-%d")
    eval_end_dt = datetime.strptime(date_range[1], '%m/%d/%Y').strftime("%Y-%m-%d")

    save_data = {
        "eval_plan_nm": req['eval_plan_nm'],
        "eval_plan_desc": req['eval_plan_desc'],
        "eval_strt_dt": eval_strt_dt,
        "eval_end_dt": eval_end_dt,
        "eval_clss": req['eval_clss'],
        "eval_sheet_no": req['eval_sheet'],
        "sf_eval_wght": req['sf_wght'],
        "s_eval_wght": req['s_wght'],
        "m_eval_wght": req['m_wght'],
        "j_eval_wght": req['j_wght'],
        "t_eval_wght": req['t_wght'],
        "p_eval_wght": req['p_wght'],
        "modf_mem_no": request.user.id
    }

    # request에 평가계획 번호가 있으면 평가 계획 수정
    if req['eval_plan_no']:
        # 이미 사용중인 평가 계획 수정 안됨
        if req["eval_clss"] == 'CC010002':
            ablt_rslt_qs = AbltEvalRslt.objects.filter(eval_plan_no=req["eval_plan_no"])
            if ablt_rslt_qs.exists():
                return render(request, 'eval_plan/eplan_error_form.html',
                              {'error': "이미 진행중인 평가 계획입니다. 수정이나 삭제할 수 없습니다."},
                              status=status.HTTP_226_IM_USED)
        # TODO: t, p kpi평가 진행 상황을 확인하는 조건 추가 해야 함

        # 수정된 평가 계획 저장
        save_data["eval_plan_no"] = req['eval_plan_no']
        eval_plan_qs = EvalPlan.objects.get(pk=req['eval_plan_no'])
        eval_plan_serializer = CreateEvalPlanSerializer(eval_plan_qs, data=save_data, partial=True)

    # request에 평가계획 번호가 없으면 평가 계획 생성
    else:
        # 신규 평가 계획 저장
        save_data["reg_mem_no"] = request.user.id
        eval_plan_serializer = CreateEvalPlanSerializer(data=save_data)

    # 수정, 생성용 데이터 검증 및 저장
    if eval_plan_serializer.is_valid():
        eval_plan_serializer.save()

        eval_plan_qs = EvalPlan.objects.filter(del_yn="N").order_by("-eval_strt_dt")
        eval_plan_serializer = GetEvalPlanSerializer(eval_plan_qs, many=True)
        return render(request, 'eval_plan/eval_plan_list.html', {"eval_plan_ls": eval_plan_serializer.data})
    else:
        return render(request, 'eval_plan/eplan_error_form.html', {'error': eval_plan_serializer.errors})


# 평가계획 삭제
@api_view(['POST'])
@permission_classes([AllowAny])
def del_eval_plan(request):
    req = request.data

    # 이미 사용 중인 평가 계획 삭제 안됨
    if req["eval_clss"] == 'CC010002':
        ablt_rslt_qs = AbltEvalRslt.objects.filter(eval_plan_no=req["eval_plan_no"])
        if ablt_rslt_qs.exists():
            return render(request, 'eval_plan/eplan_error_form.html',
                          {'error': "이미 진행중인 평가 계획입니다. 수정이나 삭제할 수 없습니다."},
                          status=status.HTTP_226_IM_USED)

    # TODO: t, p kpi 평가 결과 확인 조건 생성해야 함

    save_data = {
        "eval_plan_no": req["eval_plan_no"],
        "modf_mem_no": request.user.id,
        "del_yn": "Y"
    }

    eval_plan_qs = EvalPlan.objects.filter(pk=req["eval_plan_no"]).first()
    eval_plan_serializer = DelEvalPlanSerializer(eval_plan_qs, data=save_data, partial=True)

    if eval_plan_serializer.is_valid():
        eval_plan_serializer.save()
        eval_plan_qs = EvalPlan.objects.filter(del_yn="N").order_by("-eval_strt_dt")
        eval_plan_serializer = GetEvalPlanSerializer(eval_plan_qs, many=True)
        return render(request, 'eval_plan/eval_plan_list.html', {"eval_plan_ls": eval_plan_serializer.data})
    else:
        return render(request, 'eval_plan/eplan_error_form.html', {'error': eval_plan_serializer.errors})
