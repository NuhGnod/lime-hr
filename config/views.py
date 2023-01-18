from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render


@api_view(['GET'])
@permission_classes([AllowAny])
@login_required
def home_view(request):

    return render(request, 'main.html')