from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'files'

urlpatterns = [
    #path('admin', views.detail, name='default'),
    url(r'^$', views.index, name='index'),
]