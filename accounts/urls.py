from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'accounts'


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('change_password', change_password, name='change_password'),
    path('profile/<int:pk>', get_profile, name='profile', kwargs={'app_name': app_name, 'app_category_name': '개인정보', 'page_name': '프로필'}),
    path('profile/upload_img', upload_profile_image, name='upload_profile_image'),
    path('profile/clear_img', clear_profile_image, name='clear_profile_image')
]