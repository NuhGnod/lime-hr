
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render

from management.models import CommCd
from mdm.models import EvalPlan, EvalSheet

from mdm.serializers import (
    GetEvalPlanSerializer, GetEvalPlanDetailSerializer, GetEvalSheetSerializer, CreateEvalPlanSerializer
    )
from management.serializers import CommCdMapperSerializer
# 평가지 view


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_evaluation_plan(request, *args, **kwargs):

    eval_plan_qs = EvalPlan.objects.filter(del_yn="N")
    eval_plan_serializer = GetEvalPlanSerializer(eval_plan_qs, many=True)

    return render(request, 'eval_plan/eval_plan.html', {"eval_plan_ls": eval_plan_serializer.data})


@api_view(['POST'])
@permission_classes([AllowAny])
def get_detail_eval_plan(request):
    req = request.data.copy()
    plan_no = req['plan_no']

    # 평가 계획 상세 가져오기
    eval_plan_qs = EvalPlan.objects.filter(eval_plan_no=plan_no, del_yn='N').first()
    eval_plan_serializer = GetEvalPlanDetailSerializer(eval_plan_qs)

    # 평가지 목록 가져오기
    eval_sheet_qs = EvalSheet.objects.filter(del_yn='N')
    eval_sheet_serializer = GetEvalSheetSerializer(eval_sheet_qs, many=True)

    # 평가 구분 목록 가져오기
    eval_clss_qs = CommCd.objects.filter(hi_comm_cd='CC010000', del_yn='N')
    eval_clss_serializer = CommCdMapperSerializer(eval_clss_qs, many=True)

    return render(request, 'eval_plan/eval_plan_detail.html', {'eval_sheet_ls': eval_sheet_serializer.data,
                                                               'eval_plan_detail': eval_plan_serializer.data,
                                                               'eval_clss_ls': eval_clss_serializer.data
                                                               })


@api_view(['POST', 'PUT'])
@permission_classes([AllowAny])
def save_eval_plan(request):
    req = request.data

    date_range = [date.strip() for date in req['date_range'].split('-')]
    eval_strt_dt = date_range[0].split('/')
    eval_strt_dt = eval_strt_dt[2] + eval_strt_dt[0] + eval_strt_dt[1]
    eval_end_dt = date_range[1].split('/')
    eval_end_dt = eval_end_dt[2] + eval_end_dt[0] + eval_end_dt[1]

    save_data = {
        "eval_plan_nm": req['eval_plan_nm'],
        "eval_plan_desc": req['eval_plan_desc'],
        "eval_strt_dt": eval_strt_dt,
        "eval_end_dt": eval_end_dt,
        "eval_clss": req['eval_clss'],
        "eval_sheet": req['eval_sheet'],
        "sf_eval_wght": req['sf_wght'],
        "s_eval_wght": req['sf_wght'],
        "m_eval_wght": req['sf_wght'],
        "j_eval_wght": req['sf_wght'],
        "t_eval_wght": req['sf_wght'],
        "p_eval_wght": req['sf_wght'],
        "modf_mem_no": request.user.id
    }

    if request.method == 'POST':
        save_data['reg_mem_no'] = request.user.id

    if request.method == "PUT":
        print("==============================================")
        print(req)
        print("==============================================")
        pass



    pass