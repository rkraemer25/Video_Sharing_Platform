from django.urls import include,path
from django.conf.urls import url

import sys
import mainapp
from . import views

app_name = 'Video_Player'

urlpatterns = [
    path(r'', mainapp.views.index, name='index'),
    path(r'page1/', views.page1, name='index'),
    path(r'getmenu/', views.getmenu, name='menu'),
]
