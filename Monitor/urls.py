#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/4 17:52'

from django.conf.urls  import url
from . import views

urlpatterns=[

    url('', views.index),
    # url(r'^indexPage',views.signin),

    # url(r'^signin', views.signin),
    # url(r'^sup',views.anlysit),
    # url(r'^one',views.anlysit2),
    # url(r'^many', views.anlysit3),
    # url(r'^febakCarPoints', views.febakCarPoints),
    # url(r'^carNum', views.carNumber),
    # url(r'^febakSuppiles', views.febakSupplies),
    # url(r'^pointSup', views.supPointsTest),
    # url(r'^xcheckSingn',views.checkSingin),

]
