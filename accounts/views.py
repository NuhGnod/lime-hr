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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request, pk, *args, **kwargs):
    qs = EusoMem.objects.get(pk=pk)

    print("==================")
    print(qs)
    print("==================")
    return render(request, "auth/profile.html", {'mem_detail': qs})


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


def logout(request):
    auth.logout(request)
    return redirect('main')
