from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.urls import reverse
from management.serializers import *

@api_view(['POST', 'GET', 'DELETE'])
@permission_classes([AllowAny])
@csrf_exempt
def code(req):
    test = req.data.copy()
    test['update_user'] = req.user.id
    if req.method == 'GET':
        codes = CommCd.objects.all()
        # codes = ABCD.objects.filter(del_yn='N')
        serializer = CommCdSerializer(codes, many=True)
        listt = {
            'comm_cd':"",
        }
        return render(req, 'code/common_code.html', {'code_list': serializer.data, 'list': listt })
    if req.method == 'DELETE':
        try:
            old_id = test['comm_cd']
            obj = CommCd.objects.get(comm_cd=old_id)
            serializer = CommCdSerializer(obj, data=test, partial=True)
            serializer.is_valid()
            serializer.save()
            req.method = 'GET'
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_410_GONE)

    if req.method == 'POST':
        try:
            old_id = test['comm_cd']
            obj = CommCd.objects.get(comm_cd=old_id) # 존재하지않으면 doesnotexist 예외처리 -> except구문
            #obj가 존재하는 경우 == 이미 있는 코드 => 수정 로직
            serializer = CommCdSerializer(obj, data=test, partial=True)
            serializer.is_valid()
            serializer.save()
            return redirect(reverse('management:code'), req)
        except:
            serializer = CommCdSerializer(data=req.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return redirect(reverse('management:code'), req)


@api_view(['GET'])
@permission_classes([AllowAny])
@csrf_exempt
def code_list(req):
    comm_cd = req.GET['comm_cd']
    data = CommCd.objects.filter(comm_cd=comm_cd)
    serializer = CommCdSerializer(data, many=True)
    return render(req, 'code/code_put.html', {'list': serializer.data,})

@api_view(['GET'])
@permission_classes([AllowAny])
def code_add(req):
    listt = {
        'comm_cd': "",
    }
    return render(req, 'code/code_put.html', {'list': listt})