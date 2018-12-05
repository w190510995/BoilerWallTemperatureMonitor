#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/4 17:52'

from django.conf.urls import url, include
from . import views


urlpatterns=[

    url('', views.index),
    # url(r'^indexPage',views.signin),
    # url(r'^signin', views.signin),
]
