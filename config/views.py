from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render


@api_view(['GET'])
@permission_classes([AllowAny])
@login_required
def home_view(request):

    return render(request, 'main.html')


def bad_request(request, exception):
    context = {}
    return render(request, 'errors/400.html', context, status=400)


def permission_denied(request, exception):
    context = {}
    return render(request, 'errors/403.html', context, status=403)


def page_not_found(request, exception):
    context = {}
    return render(request, 'errors/404.html', context, status=404)


def server_error(request):
    context = {}
    return render(request, 'errors/500.html', context, status=500)


def csrf_failure(request, reason=""):
    context = {}
    return render(request, 'errors/403.html', context, status=403)