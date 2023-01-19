

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_evaluation_item(request, *args, **kwargs):
    print(kwargs)
    result = dict(sheet="123123",**kwargs)
    return render(request, 'eval_item/eval_item.html', result)
