#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/22 14:07'
from django.core.cache  import cache


def catchTe():
    cache.set('tag23',{"name":"wangsssssssssssss","age":20})
    print('>>>>>>>>>>>>::::::::::',cache.get('t32'))

