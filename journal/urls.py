from django.urls import path, re_path
from .views import *

app_name = 'journal'
app_category_name = "업무일지"

urlpatterns = [
    path('<int:pk>', get_all_journal, name='journal',
         kwargs={'app_name': app_name, 'app_category_name': app_category_name, 'page_name': '업무일지'}),
]
