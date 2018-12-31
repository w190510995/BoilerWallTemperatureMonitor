#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/31 22:41'


def SecondsToHMS(seconds):

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    return  str(h)+'时'+str(m)+'分'+str(s)+'秒'