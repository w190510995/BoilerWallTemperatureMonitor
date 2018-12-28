#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/22 14:07'
from django.core.cache import cache
import datetime

def catchTe():
    # cache.set('tag23',{"name":"wangsssssssssssss","age":20})
    # print('>>>>>>>>>>>>::::::::::',cache.get('t32'))
    try:

        print(cache.get('myGroup.20BY-0001'))
    except Exception as e:
        print(e)
        print("未获取到redis数据")



