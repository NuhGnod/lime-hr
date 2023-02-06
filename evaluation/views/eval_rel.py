from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from django.db.models import Q

from accounts.models import EusoMem
from management.models import EusoDept, CommCd, EusoPjt, PjtJoinHist
from accounts.serializers import GetEusoMemSerializer
from management.serializers import CommCdMapperSerializer, GetEusoDeptSerializer, GetPjtListSerializer



@api_view(["GET"])
@permission_classes([AllowAny])
def get_eval_relation_main(request, *args, **kwargs):
    contents = dict(**kwargs)
    # TODO: 일반 사원이라면 사원 명을 평가자로 고정, 관리자라면 평가자 고정 안함
    # TODO: 기존에 설정했던 평가 관계가 있다면 함께 반환
    # TODO: 기존에 설정했던 평가 관계가 없다면 빈 데이터 반환

    # 사원 목록 가져오기
    euso_mem_qs = EusoMem.objects.filter(del_yn="N")
    euso_mem_serializer = GetEusoMemSerializer(euso_mem_qs, many=True)
    contents.update(euso_mem_list=euso_mem_serializer.data)

    # 부서 그룹 가져오기
    comm_cd_qs = CommCd.objects.filter(hi_comm_cd="CC017000", del_yn="N")
    comm_cd_serializer = CommCdMapperSerializer(comm_cd_qs, many=True)
    contents.update(dept_grp_ls=comm_cd_serializer.data)

    # 부서 목록 가져오기
    dept_qs = EusoDept.objects.filter(del_yn="N", hi_dept_no=None)
    dept_serializer = GetEusoDeptSerializer(dept_qs, many=True)
    contents.update(dept_ls=dept_serializer.data)

    # 프로젝트 목록 가져오기
    pjt_qs = EusoPjt.objects.filter(del_yn="N")
    pjt_serializer = GetPjtListSerializer(pjt_qs, many=True)
    contents.update(pjt_ls=pjt_serializer.data)

    return render(request, "eval_rel/eval_rel_main.html", contents)


@api_view(["POST"])
@permission_classes([AllowAny])
def get_erel_pjt_mem_list(request):
    req = request.data
    contents = dict()

    if req["filter"] == "pjt" and req["pjt_no"] == "all":
        pjt_join_hist_mem_ls = PjtJoinHist.objects.filter(del_yn="N").values_list("mem_no__id").distinct()

    elif req["pjt_no"] != "all":
        pjt_no = req["pjt_no"]
        pjt_join_hist_mem_ls = PjtJoinHist.objects.filter(del_yn="N", pjt_no=pjt_no).values_list("mem_no__id").distinct()

    else:
        return render(request, "eval_rel/eval_mem_list.html", contents, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    euso_mem_qs = EusoMem.objects.filter(del_yn="N", id__in=pjt_join_hist_mem_ls)

    # 사원 목록 가져오기
    euso_mem_serializer = GetEusoMemSerializer(euso_mem_qs, many=True)
    contents.update(euso_mem_list=euso_mem_serializer.data)

    return render(request, "eval_rel/eval_mem_list.html", contents)


@api_view(["POST"])
@permission_classes([AllowAny])
def get_erel_tree_mem_list(request):
    req = request.data
    group_cd = req["group_cd"]
    dept_no = req["dept_no"]
    contents = dict()

    if req["filter"] == "tree" and group_cd == "all" and dept_no == "all":
        # 사원 목록 가져오기
        euso_mem_qs = EusoMem.objects.filter(del_yn="N")

    elif group_cd != "all" and dept_no == "all" :
        dept_no_ls = EusoDept.objects.filter(del_yn="N", dept_cd=group_cd).values_list("dept_no").distinct()
        euso_mem_qs = EusoMem.objects.filter(del_yn="N", dept_no__in=dept_no_ls)

    elif group_cd != "all" and dept_no != "all":
        q = Q()
        q.add(Q(del_yn="N"), q.AND)
        q.add(Q(dept_no=dept_no) | Q(hi_dept_no=dept_no), q.AND)
        dept_no_ls = EusoDept.objects.filter(q).values_list("dept_no").distinct()
        euso_mem_qs = EusoMem.objects.filter(del_yn="N", dept_no__in=dept_no_ls)

    else:
        return render(request, "eval_rel/eval_mem_list.html", contents,
                      status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    euso_mem_serializer = GetEusoMemSerializer(euso_mem_qs, many=True)
    contents.update(euso_mem_list=euso_mem_serializer.data)
    return render(request, "eval_rel/eval_mem_list.html", contents)


# TODO: 피 평가자 저장