from django.urls import path, re_path
from management.views.pjt import get_all_pjt

app_name = 'management'

urlpatterns = [
    path('pjt/', get_all_pjt, name='pjt_list'),
    # path('code/', get_all_code, name='code_list'),
    path('code/', code, name='code'),
    # path('code/', ddlCode, name='modify_code')
    path('code/list', code_list, name='code_list'),
    path('code/add', code_add, name='code_add'),

    # path('code/button')
    # path('code/<String:pk>', code, name='code'),
]