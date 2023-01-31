from django.urls import path, re_path
from .views import *

app_name = 'evaluation'
app_category_name = "평가"

urlpatterns = [
    path('desc', evaluation_main, name='eval', kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '역량평가'}),
    path('form/<int:pk>/', get_all_evaluation, name='eval_form', kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '역량평가'}),
    path('form/<int:pk>/insert', insert_evaluation_form, name='eval_form_submit', kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '역량평가'}),
    path('form/complete', complete_evaluation, name='eval_complete', kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '역량평가'}),

]
