
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse
# 평가지 view


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_evaluation_sheet(request, *args, **kwargs):
    print(kwargs)
    result = dict(sheet="123123",**kwargs)
    return render(request, 'eval_sheet/eval_sheet.html',result)


@api_view(['GET'])
@permission_classes([AllowAny])
def ajax_sample(request):
    print(request.GET.get('value'))
    result = dict(test="ssssssss")
    return JsonResponse(result)
