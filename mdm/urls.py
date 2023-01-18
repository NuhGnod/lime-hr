from django.urls import path, re_path
from mdm.views import *

app_name = 'mdm'
app_category_name = '기준정보 관리'

urlpatterns = [
    path('esheet/', get_all_evaluation_sheet, name='eval_sheet_list', kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '평가지관리'}),

    # 비동기 요청
    path('ajax/test', ajax_sample, name='ajax_sample')
]
