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
    url(r'^postClassic', views.persisteOpreation),
    url(r'^getClassic',views.getOpreation),
    url(r'^getRealAlerm',views.geteRaalAlarmData),
    url(r'^getHistoryData',views.getHistoryDatae),
    url(r'^getAssessData',views.getOpreationAseete),
    # url(r'^signin', views.signin),
    url(r'^users',views.resUsers),
    url(r'^currentUser',views.resCurentUser),
    url(r'^curentCunter',views.getCurentCunter), #当前报警条数
    url(r'^monthsCunter',views.getMonthsCunter), #当前报警条数
    url(r'^allCunter',views.getAllClassicCunter), #当月报警条数统计
]

catchTe();