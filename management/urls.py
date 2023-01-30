from django.urls import path, re_path
from management.views.pjt import (
    get_all_pjt, get_join_pjt_member, create_pjt_join_hist_member, delete_pjt_join_hist_member, create_pjt
    )
from management.views import code, code_list, code_add

app_name = 'management'

urlpatterns = [
    path('pjt/', get_all_pjt, name='pjt_list'),
    path('code/', code, name='code'),
    path('code/list', code_list, name='code_list'),
    path('code/add', code_add, name='code_add'),




    # ajax api
    path('pjtJoin/create/', create_pjt_join_hist_member, name='create_pjt_join_hist'),
    path('pjtJoin/delete/', delete_pjt_join_hist_member, name='del_pjt_join_hist'),
    path('pjtJoin/', get_join_pjt_member, name='join_pjt_mem'),
    path('pjt/create/', create_pjt, name='create_pjt')
    ]