from django.urls import path, re_path
from mdm.views import *

from mdm.views.eval_plan import get_all_evaluation_plan, get_detail_eval_plan, save_eval_plan

app_name = 'mdm'
app_category_name = '기준정보 관리'

urlpatterns = [
    # 평가지 관리 메인 이동
    path('esheet/', sheet, name='eval_sheet',
         kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '평가지관리'}),
    path('esheet/modal', modal, name="modal"),
    path('esheet/eval_ques', eval_ques_delete, name="eval_ques_delete"),
    path('esheet/eval_sheet', create_eval_sheet, name="eval_sheet_add"),

    # 평가항목 관리 메인 이동
    path('eitem/', get_all_evaluation_item, name='eval_item',
         kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '평가항목관리'}),

    # 평가계획 관리 메인 이동
    path('eplan/', get_all_evaluation_plan, name='eval_plan',
         kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '평가계획관리'}),
    
    # 비동기 요청
    path('ajax/test', ajax_sample, name='ajax_sample'),
    path('eplan/detail/', get_detail_eval_plan, name='eplan_detail'),
    path('eplan/save', save_eval_plan, name='eplan_save'),
    path('eplan/save', save_eval_plan, name='eplan_save'),


    # 평가문항 관리 메인 이동
    path('eques/', get_all_question, name='eval_ques', kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '평가문항관리'}),
    path('eques/add', ajax_add_question, name='add_question'),
    path('eques/ques', get_question, name='get_question'),
    path('eques/save', save_question, name='save_question'),
    path('eques/eitem', ajax_get_eval_item, name='get_eval_item'),

]
