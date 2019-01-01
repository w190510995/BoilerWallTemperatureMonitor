#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/26 17:57'
from django.core.cache  import cache
from datetime import datetime
from Monitor.models import TempratureAlermValue
from Api import utilsTools

#name:标签名
#value: 标签当前值
#thresholdValuet：区域定值
def dataProcess(name,value,thresholdValuet,area):

    get_value_catch = cache.get(name) #根据标签名获取redis中对应的数据

    if get_value_catch is None: # redis中无标签对应的数据，则新建一条数据缓存到redis


        if value >= thresholdValuet: #标签当前值大于定值

                # 超过定值，放入redis
                cache.set(name, {
                    'curentValue': value, #当前值
                    'maxValue': value, #最大值，第一次最大值为当前值
                    'thresholdValuet': thresholdValuet,
                    'beginDate': datetime.now(),
                    'area':area,
                    'endDate': '',
                    'status': 1  # 1：报警  0:报警结束
                },
                 timeout=None,  # 永不超时
                )


    else:

        if get_value_catch['status'] == 1: #  1：报警未结束
            if value >= thresholdValuet: #大于定值 更新缓存maxvalue数据
                maxValue = get_value_catch['maxValue']

                if value > maxValue:
                    get_value_catch['maxValue'] = value  # 更新状态

                get_value_catch['curentValue'] = value  # 更新状态
                cache.set(name, get_value_catch, timeout=None)  # 更新数据到redis

            else:
                get_value_catch['status'] = 0  # 更新状态
                get_value_catch['endDate'] = datetime.now()  # 结束日期
                cache.set(name, get_value_catch, timeout=None)  # 更新数据到redis

        elif get_value_catch['status'] == 0:  #该条报警状态已结束，保存到数据库，随后删除redis中数据

            beginTime1 = get_value_catch['beginDate'],
            endTime1 = get_value_catch['endDate'],

            persistence = TempratureAlermValue(
                name=name,
                area=get_value_catch['area'],
                classic= utilsTools.OPREATION_CLASSIC,
                maxValue= get_value_catch['maxValue'],
                thresholdValuet= get_value_catch['thresholdValuet'],
                beginTime= get_value_catch['beginDate'],
                endTime= get_value_catch['endDate'],
                tiemDiff= (endTime1[0]-beginTime1[0]).seconds
            )
            persistence.save() #保存到数据库
            cache.delete(name)  # 报警结束 删除缓存






