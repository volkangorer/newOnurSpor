from . import views

from django.contrib import admin
from django.urls import path,include


app_name = "user"

urlpatterns = [
    path('login/', views.loginUser,name = "login"),
    path('logout/', views.logoutUser,name = "logout"),
]