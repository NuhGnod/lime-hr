from django.urls import path, re_path
from .views import *
from .views.eval_rel import *

app_name = 'evaluation'
app_category_name = "평가"

urlpatterns = [
    path('desc', evaluation_main, name='eval', kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '역량평가'}),
    path('form/<int:pk>/', get_all_evaluation, name='eval_form', kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '역량평가'}),
    path('form/<int:pk>/insert', insert_evaluation_form, name='eval_form_submit', kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '역량평가'}),
    path('form/complete', complete_evaluation, name='eval_complete', kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '역량평가'}),
    
    #평가 결과관리
    path('rslt', get_evaluation_rslt, name='eval_rslt', kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '평가결과관리'}),
    path('rslt/rslt_excel_download', excel_download, name='rslt_excel_download'),

    # 평가 관계관리
    path('eRel/', get_eval_relation_main, name='eval_rel', kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '평가관계관리'}),
    path('eRel/pjtAjax', get_erel_pjt_mem_list, name='rel_pjt_mem_ls'),
    path('eRel/treeAjax', get_erel_tree_mem_list, name='rel_tree_mem_ls'),

]
