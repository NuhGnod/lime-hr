from django.urls import path, re_path
from mdm.views import *

app_name = 'mdm'
app_category_name = '기준정보 관리'

urlpatterns = [
    # 평가지 관리 메인 이동
    path('esheet/', get_all_evaluation_sheet, name='eval_sheet',
         kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '평가지관리'}),
    
    # 평가항목 관리 메인 이동
    path('eitem/', get_all_evaluation_item, name='eval_item',
         kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '평가항목관리'}),
    
    # 평가계획 관리 메인 이동
    path('eplan/', get_all_evaluation_plan, name='eval_plan',
         kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '평가계획관리'}),
    
    # 비동기 요청
    path('ajax/test', ajax_sample, name='ajax_sample')
]
