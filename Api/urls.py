#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/4 17:52'

from django.conf.urls import url, include
from . import views
from  Api.catchTest import catchTe


urlpatterns=[

    url(r'^index', views.index),
    url(r'^getGrq', views.get_grq_mean_value),
    # url(r'^indexPage',views.signin),
    # url(r'^signin', views.signin),
]

catchTe();