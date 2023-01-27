from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse

from management.models import EusoPjt, CommCd

from management.serializers import EusoPjtSerializer, CommCdMapperSerializer


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_all_pjt(request):
    # temp_pjt_ls = [{'pjt_no': 1, 'pjt_nm': 'kistep 다차원 네트워크 분석', 'start_dt': '2023-01-01', 'end_dt': '2023-07-07'},
    #                {'pjt_no': 2, 'pjt_nm': '인사평가 시스템', 'start_dt': '2023-01-01', 'end_dt': '2023-07-07'},
    #                {'pjt_no': 3, 'pjt_nm': 'cctv tracking', 'start_dt': '2023-01-01', 'end_dt': '2023-07-07'}]

    # 프로젝트 목록 가져오기
    pjt_obj = EusoPjt.objects.all()
    pjt_serializer = EusoPjtSerializer(pjt_obj, many=True)\



    return render(request, 'pjt/pjt_main.html', {'pjt_list': pjt_serializer.data})


@api_view(['GET'])
@permission_classes([AllowAny])
def ajax_get_pjt_member(request):
    """프로젝트에 속한 인력 목록 반환"""

    pjt_member = {
        1: {'mem_nm': '송재익', 'role_cd': 'PM', 'enter_dt': '2023-01-01', 'out_dt': '2023-01-31'},
        2: {'mem_nm': '송재익', 'role_cd': 'PL', 'enter_dt': '2023-01-01', 'out_dt': '2023-01-31'},
        3: {'mem_nm': '김민교', 'role_cd': '개발자', 'enter_dt': '2023-01-01', 'out_dt': '2023-01-31'},
        4: {'mem_nm': '김동훈', 'role_cd': '개발자', 'enter_dt': '2023-01-01', 'out_dt': '2023-01-31'},
        5: {'mem_nm': '이주희', 'role_cd': '개발자', 'enter_dt': '2023-01-01', 'out_dt': '2023-01-31'},
    }
    return JsonResponse(pjt_member)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def ajax_pjt_join_member(request):
    pjt_no = request.data["pjt_no"]
    print("===============================")
    print("request.data : ", request.data["pjt_no"])
    print("===============================")

    # 프로젝트 역할 코드 가져오기
    role_cd_obj = CommCd.objects.filter(hi_comm_cd='CC004000')
    role_cd_serializer = CommCdMapperSerializer(role_cd_obj, many=True)
    return render(request, 'pjt/pjt_join_mem.html', {'role_list': role_cd_serializer.data, 'pjt_no': pjt_no})