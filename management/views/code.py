from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from rest_framework.response import Response

from management.models import CommonCode, CCode
from management.serializers import *

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def get_all_code(request):
#     code_list = [dict(comm_cd="CC001001", comm_cd_nm="코드명1"), dict(comm_cd="CC001002", comm_cd_nm="코드명2")]
#     return render(request, 'code/code_list.html', {'code_list': code_list})
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def code(req):
    print(req.data)
    if req.method == 'GET':
        codes = CC2.objects.all()
        serializer = CC2Serializer(codes, many=True)
        print(serializer.data)
        return render(req, 'code/code_list.html', {'code_list': serializer.data})

    if req.method == 'POST':
        print("POSTPOSTPOSTPOSTPOST")
        print(req.data)
        serializer = CC2Serializer(data=req.data, partial=True)
        # serializer.se

        serializer.is_valid()
        serializer.save()
        return render(req, '../templates/main.html')
        # return Response(req.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def code(req, pk):
    print(req.data)

    if req.method == 'PUT':
