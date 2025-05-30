

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name=""),
    
    path('register', views.register, name="register"),
    
    path('my-login', views.my_login, name="my-login"),
    
    path('user-logout', views.user_logout, name="user-logout"),
    
    path('dashboard', views.dashboard, name="dashboard"),
]