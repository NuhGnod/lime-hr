from django.urls import path, re_path
from .views import get_all_evaluation
app_name = 'evaluation'


urlpatterns = [
    path('eval_desc/', get_all_evaluation, name='eval_desc'),
]