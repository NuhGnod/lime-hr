from django.shortcuts import render
from django.views.generic import FormView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import EusoMem
from django.contrib import auth
from management.models import CommCd
from django.contrib.auth.hashers import check_password
from uuid import uuid4
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request, pk, *args, **kwargs):
    qs = EusoMem.objects.get(pk=pk)

    return render(request, "profile/profile.html", {'mem_detail': qs, **kwargs})


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            posi_nm = CommCd.objects.get(comm_cd=user.posi_cd).cd_nm
            duty_resp_nm = CommCd.objects.get(comm_cd=user.duty_resp_cd).cd_nm

            request.session['posi_nm'] = posi_nm
            request.session['duty_resp_nm'] = duty_resp_nm
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, "auth/login.html", {'error': "회원ID와 비밀번호가 일치하지 않습니다."})
    else:
        return render(request, 'auth/login.html')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    param = request.data.copy()
    print(param)
    result = dict()
    current_password = param['origin_password']
    user = request.user
    if check_password(current_password, user.password):
        new_password = param['password_1']
        password_confirm = param['password_2']
        if new_password == password_confirm:
            user.set_password(new_password)
            user.save()
            auth.login(request, user)
            result.update(is_error=False, msg='비밀번호 변경에 성공하였습니다.')
        else:
            result.update(is_error=True, target='password1', msg='비밀번호와 확인 비밀번호가 일치하지 않습니다.')
    else:
       result.update(is_error=True, target='origin_password', msg='현재 비밀번호와 일치하지 않습니다.')
    return JsonResponse(result)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_profile_image(request):
    result = dict(is_success=False)
    if request.FILES:

        profile_img = request.FILES['profile_img']
        user = request.user
        user_qs = EusoMem.objects.get(pk=user.id)

        uuid = uuid4().hex
        ext = profile_img.name.split('.')[-1]

        filename = '{}.{}'.format(uuid, ext)

        profile_img.name = filename

        user_qs.profile_img = profile_img

        user_qs.save()
        result.update(is_success=True)
    return JsonResponse(result)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def clear_profile_image(request):
    user = request.user
    user_qs = EusoMem.objects.get(pk=user.id)
    user_qs.profile_img = None

    user_qs.save()
    result = dict(is_success=True)
    return JsonResponse(result)


def logout(request):
    auth.logout(request)
    return redirect('main')
