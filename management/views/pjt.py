from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render, redirect

from management.models import EusoPjt, CommCd, PjtJoinHist, CsOrgn
from accounts.models import EusoMem

from management.serializers import (
    EusoPjtSerializer, CommCdMapperSerializer, GetPjtJoinMemberSerializer, CreatePjtJoinMemberSerializer,
    DelPjtJoinMemberSerializer, GetCsOrgnSerializer, CreatePjtSerializer
    )
from accounts.serializers import GetEusoMemSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_pjt(requests):
    # 프로젝트 목록 가져오기
    pjt_obj = EusoPjt.objects.all().order_by('-start_dt')
    pjt_serializer = EusoPjtSerializer(pjt_obj, many=True)

    # 기관 목록 가져오기
    cs_obj = CsOrgn.objects.filter(del_yn='N')
    cs_serializer = GetCsOrgnSerializer(cs_obj, many=True)
    return render(requests, 'pjt/pjt_main.html', {'pjt_list': pjt_serializer.data, 'cs_ls': cs_serializer.data})


@api_view(['POST'])
@permission_classes([AllowAny])
def create_pjt(requests):
    req = requests.data

    date_range = [date.strip() for date in req['date_range'].split('-')]
    start_dt = date_range[0].split('/')
    start_dt = start_dt[2] + start_dt[0] + start_dt[1]
    end_dt = date_range[1].split('/')
    end_dt = end_dt[2] + end_dt[0] + end_dt[1]

    pjt_dic = {
        "pjt_nm": req["pjt_nm"],
        "cs_no": req["cs_no"],
        "start_dt": start_dt,
        "end_dt": end_dt,
        "reg_mem_no": requests.user.id,
        "modf_mem_no": requests.user.id
    }
    pjt_serializer = CreatePjtSerializer(data=pjt_dic)
    if pjt_serializer.is_valid():
        pjt_serializer.save()

        return redirect("/manage/pjt/")

    else:
        return render(requests, 'pjt/pjt_error_form.html', {"error": pjt_serializer.errors})


@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def get_join_pjt_member(requests):
    pjt_no = requests.data["pjt_no"]

    # 회원 목록 가져오기
    euso_mem_qs = EusoMem.objects.filter(del_yn="N")
    euso_mem_serializer = GetEusoMemSerializer(euso_mem_qs, many=True)

    # 프로젝트 역할 코드 가져오기
    role_cd_qs = CommCd.objects.filter(hi_comm_cd='CC004000', del_yn='N')
    role_cd_serializer = CommCdMapperSerializer(role_cd_qs, many=True)

    # 프로젝트 참여중인 회원 목록 가져오기
    pjt_join_hist_qs = PjtJoinHist.objects.filter(pjt_no=pjt_no, del_yn='N')
    pjt_join_hist_serializer = GetPjtJoinMemberSerializer(pjt_join_hist_qs, many=True)
    return render(requests, 'pjt/pjt_join_mem.html', {'role_list': role_cd_serializer.data,
                                                     'pjt_no': pjt_no,
                                                     'mem_ls': euso_mem_serializer.data,
                                                     'pjt_mem_ls': pjt_join_hist_serializer.data,
                                                     })


@api_view(["POST"])
@permission_classes([AllowAny])
def create_pjt_join_hist_member(requests):
    req = requests.data.copy()

    date_range = [date.strip() for date in req['date_range'].split('-')]
    enter_dt = date_range[0].split('/')
    enter_dt = enter_dt[2] + enter_dt[0] + enter_dt[1]
    out_dt = date_range[1].split('/')
    out_dt = out_dt[2] + out_dt[0] + out_dt[1]

    pjt_join_hist_dic = {
        "pjt_no": req['pjt_no'],
        "mem_no": req['mem_no'],
        "role_cd": req['role_cd'],
        "enter_dt": enter_dt,
        "out_dt": out_dt,
        "reg_mem_no": requests.user.id,
        "modf_mem_no": requests.user.id
    }

    pjt_join_hist_serializer = CreatePjtJoinMemberSerializer(data=pjt_join_hist_dic)
    if pjt_join_hist_serializer.is_valid():
        pjt_join_hist_serializer.save()

        # 프로젝트 참여중인 회원 목록 가져오기
        pjt_join_hist_obj = PjtJoinHist.objects.filter(pjt_no=req['pjt_no'], del_yn='N')
        pjt_join_hist_serializer = GetPjtJoinMemberSerializer(pjt_join_hist_obj, many=True)
        return render(requests, 'pjt/pjt_mem_ls_form.html', {"pjt_mem_ls": pjt_join_hist_serializer.data})

    else:
        return render(requests, 'pjt/pjt_error_form.html', {"error": pjt_join_hist_serializer.errors})


@api_view(["POST"])
@permission_classes([AllowAny])
def delete_pjt_join_hist_member(requests):
    req = requests.data.copy()
    join_hist_no = req['join_hist_no']
    mem_no = req['mem_no']

    pjt_join_hist_dic = {
        "join_hist_no": join_hist_no,
        "mem_no": mem_no,
        "del_yn": "Y",
        "modf_mem_no": requests.user.id
    }

    pjt_join_hist_qs = PjtJoinHist.objects.get(join_hist_no=join_hist_no)
    pjt_join_hist_serializer = DelPjtJoinMemberSerializer(pjt_join_hist_qs, data=pjt_join_hist_dic)

    if pjt_join_hist_serializer.is_valid():
        pjt_join_hist_serializer.save()

        # 프로젝트 참여중인 회원 목록 가져오기
        pjt_join_hist_qs = PjtJoinHist.objects.filter(pjt_no=req['pjt_no'], del_yn='N')
        pjt_join_hist_serializer = GetPjtJoinMemberSerializer(pjt_join_hist_qs, many=True)
        return render(requests, 'pjt/pjt_mem_ls_form.html', {"pjt_mem_ls": pjt_join_hist_serializer.data})

    else:
        return render(requests, 'pjt/pjt_error_form.html', {"error": pjt_join_hist_serializer.errors})
