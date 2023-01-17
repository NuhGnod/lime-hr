from django.urls import path, re_path
from management.views import get_all_code

app_name = 'management'


urlpatterns = [
    path('code/', get_all_code, name='code_list'),
]