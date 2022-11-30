from django.contrib import admin
from django.urls import path
from .import views

app_name="user"
urlpatterns = [
    
    path("userlogin/",views.userlogin,name="userlogin"),
    path("register/",views.register,name="register"),
    path("logoutuser/",views.logoutuser,name="logoutuser"),
]