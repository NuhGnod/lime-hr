from django.shortcuts import render
from django.views.generic import FormView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import EusoMem

@api_view(['GET'])
@permission_classes([AllowAny])
def get_profile(request, pk, *args, **kwargs):
    qs = EusoMem.objects.get(pk=pk)

    print("==================")
    print(qs)
    print("==================")
    pass

