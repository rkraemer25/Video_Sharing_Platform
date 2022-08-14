from django.urls import include,path
from django.conf.urls import url

import sys
import mainapp
from . import views

app_name = 'Upload_Video'

urlpatterns = [
    path(r'', mainapp.views.index, name='index'),
    path(r'page1/', views.page1, name='index'),
    path(r'upload_video/', views.upload_video, name='upload video')
]
