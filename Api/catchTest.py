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



# Name=myGroup.20BY-0100 value=757.7
# Name=myGroup.20BY-0101 value=577.25
# Name=myGroup.20BY-0102 value=502.37
# Name=myGroup.20BY-0103 value=636.77
# Name=myGroup.20BY-0104 value=795.13
# Name=myGroup.20BY-0105 value=755.86
# Name=myGroup.20BY-0106 value=565.14
# Name=myGroup.20BY-0036 value=503.11
# Name=myGroup.20BY-0037 value=638.4
# Name=myGroup.20BY-0038 value=790.65
# Name=myGroup.20BY-0039 value=722.86
# Name=myGroup.20BY-0040 value=619.75
# Name=myGroup.20BY-0041 value=617.55
# Name=myGroup.20BY-0042 value=601.47
# Name=myGroup.20BY-0043 value=739.57
# Name=myGroup.20BY-0044 value=740.15
# Name=myGroup.20BY-0045 value=590.25
# Name=myGroup.20BY-0046 value=745.17
# Name=myGroup.20BY-0047 value=532.72
# Name=myGroup.20BY-0048 value=659.35
# Name=myGroup.20BY-0049 value=622.8
# Name=myGroup.20BY-0050 value=718.56
# Name=myGroup.20BY-0051 value=574.5
# Name=myGroup.20BY-0052 value=722.55
# Name=myGroup.20BY-0053 value=544.37
# Name=myGroup.20BY-0054 value=690.14
# Name=myGroup.20BY-0055 value=641.73
# Name=myGroup.20BY-0056 value=602.47
# Name=myGroup.20BY-0057 value=577.2
