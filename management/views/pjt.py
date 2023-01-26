from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_all_pjt(request):
    temp_pjt_ls = [{'pjt_no': 1, 'pjt_nm': 'kistep 다차원 네트워크 분석', 'start_dt': '2023-01-01', 'end_dt': '2023-07-07'},
                   {'pjt_no': 2, 'pjt_nm': '인사평가 시스템', 'start_dt': '2023-01-01', 'end_dt': '2023-07-07'},
                   {'pjt_no': 3, 'pjt_nm': 'cctv tracking', 'start_dt': '2023-01-01', 'end_dt': '2023-07-07'}]

    return render(request, 'pjt/pjt_list.html', {'pjt_list': temp_pjt_ls})