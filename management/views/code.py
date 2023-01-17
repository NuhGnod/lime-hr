from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_code(request):
    code_list = [dict(comm_cd="CC001001", comm_cd_nm="코드명1"), dict(comm_cd="CC001002", comm_cd_nm="코드명2")]

    return render(request, 'code/code_list.html', {'code_list': code_list})
