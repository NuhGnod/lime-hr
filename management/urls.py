from django.urls import path, re_path
from management.views import get_all_code
from management.views.pjt import get_all_pjt

app_name = 'management'


urlpatterns = [
    path('code/', get_all_code, name='code_list'),
    path('pjt/', get_all_pjt, name='pjt_list'),
]