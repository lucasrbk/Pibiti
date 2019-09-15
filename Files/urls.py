from django.contrib import admin
from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('admin', views.detail, name='detail'),
    path('file', views.index, name='index'),
]