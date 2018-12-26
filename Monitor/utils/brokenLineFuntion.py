#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/23 12:47'

import  numpy as np
import  matplotlib.pyplot as plt
import matplotlib as mpl
from BoilerWallTemperatureMonitor import EconomizerExportModle,\
    ProofExportModle,HorizontalFlueSideWalltModle, \
    RearShaftWallTubeModle38,RearShaftWallTubeModle51,\
    LowTemperatureSuperheaterModle,PlatenSuperheaterModle45,\
    PlatenSuperheaterModle51,HighTemperatureSuperheaterModle45,\
    HighTemperatureSuperheaterModle51,LowTemperatureReheaterModle,\
    HighTemperatureReheaterModle



#省煤器出口吊挂管数据
x1 = [0,5,10,12, 15, 20, 22,25,29.52,30] #出口压力
y1 = [260,260,300,315,335,360,370,370,370,370]#报警温度
title1 = '省煤器出口吊挂管 厂家提供数据'


#顶棚出口
x2 = [0,5,9.97,15.66,21.36,27.06,28.34,30]
y2 = [540,540,540,525,500,475,470,470]
title2 = '顶棚出口  厂家提供数据'
#水平烟道侧包墙壁
x3 = [0,5,9.87,15.51,21.15,26.79,28.02,29,30]
y3 = [540,540,540,530,520,510,505,505,505]
title3 = '水平烟道侧包墙壁  厂家提供数据'
#后竖井包墙管38
x4 = [0,4,8,9.87,15.51,21.15,26.79,28.02,30]
y4 = [540,540,540,540,535,515,505,500,500]
title4 = '后竖井包墙管38 厂家提供数据'
#后竖井包墙管51
x5 = [0,4,8,9.87,15.51,21.15,26.79,28.02,30]
y5 = [540,540,540,540,530,510,495,490,490]
title5 = '后竖井包墙管51 厂家提供数据'
#低温过热器出口
x6 = [0,4,8,9.7,15.25,20.79,26.33,27.63,30]
y6 = [575,575,575,575,560,540,520,515,515]
title6 = '低温过热器出口 厂家提供数据'

#屏式过热器45
x7 = [0,4,8,9.6,15.09,20.57,26.06,27.31,30]
y7 = [630,630,630,630,630,615,605,600,600]
title7 = '屏式过热器45 厂家提供数据'

#屏式过热器51
x8 = [0,4,8,9.6,15.09,20.57,26.06,27.31,30]
y8 = [630,630,630,630,630,620,605,600,600]
title8 = '屏式过热器51 厂家提供数据'

#高温过热器45出口
x9 = [0,4,8,9.33,14.67,20,25.34,26.58,30]
y9 = [632,632,632,632,632,612,597,594,594]
title9 = '高温过热器出口45 厂家提供数据'
#高温过热器51出口
x10 = [0,4,8,9.33,14.67,20,25.34,26.58,30]
y10 = [632,632,632,632,625,602,587,584,584]
title10 = '高温过热器出口51 厂家提供数据'


#低温再热器出口
x11 = [0,2,4.75,5.07,5.5]
y11 = [570,570,570,565,565]
title11 = '低温再热器出口 厂家提供数据'

#高温再热器出口
x12 = [0,2,4.75,5.07,5.5]
y12 = [635,635,635,630,630]
title12 = '高温再热器出口 厂家提供数据'




#省煤器出口吊管报警阈值生成函数
def economizerExportFunc(pressure):
    if pressure <= 5 :
        return 260
    elif pressure >=22:
        return 370
    else:
        return EconomizerExportModle(pressure)


#顶棚出口报警阈值生成函数
def proofExportFunc(pressure):
    if pressure <= 9.97 :
        return 540
    elif pressure >=28.34:
        return 470
    else:
        return ProofExportModle(pressure)

#水平烟道侧包墙壁报警阈值生成函数
def horizontalFlueSideWalltFunc(pressure):
    if pressure <= 9.87 :
        return 540
    elif pressure >=28.05:
        return 505
    else:
        return HorizontalFlueSideWalltModle(pressure)


#后竖井包墙管38报警阈值生成函数
def rearShaftWallTubeModle38Func(pressure):
    if pressure <= 9.87 :
        return 540
    elif pressure >=28.02:
        return 500
    else:
        return RearShaftWallTubeModle38(pressure)

#后竖井包墙管51报警阈值生成函数
def rearShaftWallTubeModle51Func(pressure):
    if pressure <= 9.87 :
        return 540
    elif pressure >=28.02:
        return 490
    else:
        return RearShaftWallTubeModle51(pressure)

#低温过热器报警阈值生成函数
def lowTemperatureSuperheaterFunc(pressure):
    if pressure <= 9.70 :
        return 575
    elif pressure >=27.63:
        return 515
    else:
        return LowTemperatureSuperheaterModle(pressure)

#屏式过热器45报警阈值生成函数
def platenSuperheaterModle45Func(pressure):
    if pressure <= 15.09 :
        return 630
    elif pressure >=27.31:
        return 600
    else:
        return PlatenSuperheaterModle45(pressure)

#屏式过热器51报警阈值生成函数
def platenSuperheaterModle51Func(pressure):
    if pressure <= 15.09 :
        return 630
    elif pressure >=27.31:
        return 600
    else:
        return PlatenSuperheaterModle51(pressure)

#高温过热器45报警阈值生成函数
def highTemperatureSuperheaterFunc45(pressure):
    if pressure <= 14.67 :
        return 632
    elif pressure >=26.58:
        return 594
    else:
        return HighTemperatureSuperheaterModle45(pressure)

#高温过热器51报警阈值生成函数
def highTemperatureSuperheaterFunc51(pressure):
    if pressure <= 9.33 :
        return 632
    elif pressure >=26.58:
        return 584
    else:
        return HighTemperatureSuperheaterModle51(pressure)


#高温再热器报警阈值生成函数
def highTemperatureReheaterFunc(pressure):
    if pressure <= 4.75 :
        return 635
    elif pressure >=5.07:
        return 630
    else:
        return HighTemperatureReheaterModle(pressure)

#低温再热器报警阈值生成函数
def lowTemperatureReheaterFunc(pressure):
    if pressure <= 4.75:
        return 570
    elif pressure >=5.07:
        return 565
    else:
        return LowTemperatureReheaterModle(pressure)





def dataFit(x,y,title):
    plt.title(title)
    plt.plot(x, y)
    plt.savefig('./images/'+title+'.png', format='png')
    plt.show()




def  tset():
    dataR = x4
    list = []
    for v in dataR:
        #economizerExportFunc  省煤器出口吊管报警阈值生成函数
        # proofExportFunc  顶棚出口报警阈值生成函数
        # horizontalFlueSideWalltFunc  水平烟道侧包墙壁报警阈值生成函数
        # rearShaftWallTubeModle38Func  后竖井包墙管38报警阈值生成函数
        # rearShaftWallTubeModle51Func  后竖井包墙管51报警阈值生成函数
        # lowTemperatureSuperheaterFunc  低温过热器报警阈值生成函数
        # platenSuperheaterModle45Func  屏式过热器45报警阈值生成函数
        # platenSuperheaterModle51Func  屏式过热器51报警阈值生成函数
        # highTemperatureSuperheaterFunc45  高温过热器45报警阈值生成函数
        # highTemperatureSuperheaterFunc51  高温过热器51报警阈值生成函数
        # highTemperatureReheaterFunc  高温再热器报警阈值生成函数
        # lowTemperatureReheaterFunc  低温再热器报警阈值生成函数
        target = rearShaftWallTubeModle38Func(v)#根据区域替换
        list.append(target)
        print('tag>>  '+str(v)+'  ',target)
    # dataFit(dataR,list,'高温过热器45  拟合函数')

#
# if __name__ == '__main__':
#     # 解决中文乱码问题
#     mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体 SimHei为黑体
#     mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
#     # dataFit(x1, y1, title1)
#     # dataFit(x2, y2, title2)
#     # dataFit(x3, y3, title3)
#     # dataFit(x4, y4, title4)
#     # dataFit(x5, y5, title5)
#     # dataFit(x6, y6, title6)
#     # dataFit(x7, y7, title7)
#     # dataFit(x8, y8, title8)
#     # dataFit(x9, y9, title9)
#     # dataFit(x10, y10, title10)
#     # dataFit(x12, y12, title12)
#     # dataFit(x11, y11, title11)
#
#     tset()

