from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import static
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'files'

urlpatterns = [
    #path('admin', views.detail, name='default'),
    url(r'^$', views.index, name='index'),
    url(r'files/add_file/$', views.FileAdd.as_view(), name='add_file')
]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)