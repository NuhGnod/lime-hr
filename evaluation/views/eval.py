from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_evaluation(request):

    return render(request, 'eval/eval_complete_message.html')
