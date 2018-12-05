#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/5 15:01'


from django.conf.urls import url, include
from . import api_views

urlpatterns=[

    # url(r'^index', views.index),
    url(r'^opcRealList$',api_views.opc_real_list),

]
