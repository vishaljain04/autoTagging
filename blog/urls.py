from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('tables/', views.temp),
    path('login/', views.loginfunc),
]
