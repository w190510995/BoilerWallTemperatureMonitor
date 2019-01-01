#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/31 22:41'
import datetime,calendar
from Monitor import models


#
OPREATION_CLASSIC = models.OpreationCate.objects.get(id=1).classic

#将输入的秒，转为时分秒
def SecondsToHMS(seconds):

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    return  str(h)+'时'+str(m)+'分'+str(s)+'秒'

#输入年月，返回该月第一天及最后一天
def MonthsProcess(str1):
    temp = str1.split('-')
    months_begin = datetime.datetime.strptime(str1, '%Y-%m')
    lastDay = calendar.monthrange(int(temp[0]), int(temp[1]))[1]  # 获得该月最后一天
    end_str = temp[0] + '-' + temp[1] + '-' + str(lastDay) + ' 23:59:59'
    months_end = datetime.datetime.strptime(end_str, '%Y-%m-%d %X')

    return {
        'mBegin':months_begin,
        'mEnd':months_end,
    }

