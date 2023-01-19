from django.urls import path, re_path
from management.views import code

app_name = 'management'

urlpatterns = [
    # path('code/', get_all_code, name='code_list'),
    path('code/', code, name='code'),
    # path('code/<String:pk>', code, name='code'),
]