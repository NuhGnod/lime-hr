from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_all_pjt(request):
    temp_pjt_ls = [{'pjt_no': 1, 'pjt_nm': 'kistep 다차원 네트워크 분석', 'start_dt': '2023-01-01', 'end_dt': '2023-07-07'},
                   {'pjt_no': 2, 'pjt_nm': '인사평가 시스템', 'start_dt': '2023-01-01', 'end_dt': '2023-07-07'},
                   {'pjt_no': 3, 'pjt_nm': 'cctv tracking', 'start_dt': '2023-01-01', 'end_dt': '2023-07-07'}]

    return render(request, 'pjt/pjt_list.html', {'pjt_list': temp_pjt_ls})


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
