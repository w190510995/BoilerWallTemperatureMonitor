#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/23 14:51'
import  numpy as np


#通过锅炉厂家提供的原始数据拟合出函数

#省煤器出口吊挂管数据
x1 = [5,10,12, 15, 20, 22,25,29.52] #出口压力
y1 = [260,300,315,335,360,370,370,370]#报警温度
title1 = '省煤器出口吊挂管 厂家提供数据'
#顶棚出口
x2 = [9.97,15.66,21.36,27.06,28.34]
y2 = [540,525,500,475,470]
title2 = '顶棚出口 厂家提供数据'
#水平烟道侧包墙壁
x3 = [9.87,15.51,21.15,26.79,28.02]
y3 = [540,530,520,510,505]
title3 = '水平烟道侧包墙壁 厂家提供数据'
#后竖井包墙管38
x4 = [9.87,15.51,21.15,26.79,28.02]
y4 = [540,535,515,505,500]
title4 = '后竖井包墙管38 厂家提供数据'
#后竖井包墙管51
x5 = [9.87,15.51,21.15,26.79,28.02]
y5 = [540,530,510,495,490]
title5 = '后竖井包墙管51 厂家提供数据'
#低温过热器出口
x6 = [9.7,15.25,20.79,26.33,27.63]
y6 = [575,560,540,520,515]
title6 = '低温过热器出口 厂家提供数据'
#屏式过热器45
x7 = [9.6,15.09,20.57,26.06,27.31]
y7 = [630,630,615,605,600]
title7 = '屏式过热器45 厂家提供数据'
#屏式过热器51
x8 = [9.6,15.09,20.57,26.06,27.31]
y8 = [630,630,620,605,600]
title8 = '屏式过热器51 厂家提供数据'
#高温过热器45出口
x9 = [9.33,14.67,20,25.34,26.58]
y9 = [632,632,612,597,594]
title9 = '高温过热器出口 厂家提供数据'
#高温过热器51出口
x10 = [9.33,14.67,20,25.34,26.58]
y10 = [632,625,602,587,584]
title10 = '高温过热器出口51 厂家提供数据'
#低温再热器出口
x11 = [4.75,5.07]
y11 = [570,565]
title11 = '低温再热器出口 厂家提供数据'

#高温再热器出口
x12 = [4.75,5.07]
y12 = [635,630]
title12 = '高温再热器出口 厂家提供数据'









#生成过热器出口温度报警拟合模型
def economizerExportModle():
    z = np.polyfit(x1, y1, 14)
    modul = np.poly1d(z)
    return modul

#顶棚出口温度报警拟合模型
def proofExportModle():
    z = np.polyfit(x2, y2, 9)
    modul = np.poly1d(z)
    return modul

#水平烟道侧包墙壁温度报警拟合模型
def horizontalFlueSideWalltModle():
    z = np.polyfit(x3, y3, 9)
    modul = np.poly1d(z)
    return modul

#后竖井包墙管38温度报警拟合模型
def rearShaftWallTubeModle38():
    z = np.polyfit(x4, y4,30)
    modul = np.poly1d(z)
    return modul

#后竖井包墙管51温度报警拟合模型
def rearShaftWallTubeModle51():
    z = np.polyfit(x5, y5,8)
    modul = np.poly1d(z)
    return modul

#低温过热器温度报警拟合模型
def lowTemperatureSuperheaterModle():
    z = np.polyfit(x6, y6,10)
    modul = np.poly1d(z)
    return modul


#屏式过热器温度报警拟合模型45
def platenSuperheaterModle45():
    z = np.polyfit(x7, y7,5)
    modul = np.poly1d(z)
    return modul
#屏式过热器温度报警拟合模型51
def platenSuperheaterModle51():
    z = np.polyfit(x8, y8,5)
    modul = np.poly1d(z)
    return modul

#高温过热器45温度报警拟合模型
def highTemperatureSuperheaterModle45():
    z = np.polyfit(x9, y9,3)
    modul = np.poly1d(z)
    return modul
#高温过热器51温度报警拟合模型
def highTemperatureSuperheaterModle51():
    z = np.polyfit(x10, y10,3)
    modul = np.poly1d(z)
    return modul


#低温再热器温度报警拟合模型
def lowTemperatureReheaterModle():
    z = np.polyfit(x11, y11,6)
    modul = np.poly1d(z)
    return modul
#高温过热器温度报警拟合模型
def highTemperatureReheaterModle():
    z = np.polyfit(x12, y12,6)
    modul = np.poly1d(z)
    return modul


#返回模型
def intfunc1():
    EconomizerExportModle = economizerExportModle()
    ProofExportModle = proofExportModle()
    HorizontalFlueSideWalltModle = horizontalFlueSideWalltModle()
    RearShaftWallTubeModle38 = rearShaftWallTubeModle38()
    RearShaftWallTubeModle51 = rearShaftWallTubeModle51()
    LowTemperatureSuperheaterModle = lowTemperatureSuperheaterModle()
    PlatenSuperheaterModle45 = platenSuperheaterModle45()
    PlatenSuperheaterModle51 = platenSuperheaterModle51()
    HighTemperatureSuperheaterModle45 = highTemperatureSuperheaterModle45()
    HighTemperatureSuperheaterModle51 = highTemperatureSuperheaterModle51()
    LowTemperatureReheaterModle = lowTemperatureReheaterModle()
    HighTemperatureReheaterModle = highTemperatureReheaterModle()
    return [
        EconomizerExportModle,
        ProofExportModle,
        HorizontalFlueSideWalltModle,
        RearShaftWallTubeModle38,
        RearShaftWallTubeModle51,
        LowTemperatureSuperheaterModle,
        PlatenSuperheaterModle45,
        PlatenSuperheaterModle51,
        HighTemperatureSuperheaterModle45,
        HighTemperatureSuperheaterModle51,
        LowTemperatureReheaterModle,
        HighTemperatureReheaterModle,
    ]



# EconomizerExportModle = economizerExportModle()
# ProofExportModle = proofExportModle()
# HorizontalFlueSideWalltModle = horizontalFlueSideWalltModle()
# RearShaftWallTubeModle38 = rearShaftWallTubeModle38()
# RearShaftWallTubeModle51 = rearShaftWallTubeModle51()
# LowTemperatureSuperheaterModle = lowTemperatureSuperheaterModle()
# PlatenSuperheaterModle45 = platenSuperheaterModle45()
# PlatenSuperheaterModle51 = platenSuperheaterModle51()
# HighTemperatureSuperheaterModle45 = highTemperatureSuperheaterModle45()
# HighTemperatureSuperheaterModle51 = highTemperatureSuperheaterModle51()
# LowTemperatureReheaterModle = lowTemperatureReheaterModle()
# HighTemperatureReheaterModle = highTemperatureReheaterModle()