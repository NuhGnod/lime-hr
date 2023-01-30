from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'accounts'


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('profile/<int:pk>', get_profile, name='profile')
]