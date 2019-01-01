
from apscheduler.schedulers.background import BackgroundScheduler
from Monitor.sched.TempratureHandle import temperatureMonitorHandle
from Monitor import models

from ..config import   SCHEDULER_INTERVAL,\
    UpperWaterWall_Area_2,HorizontalFlueSideWaterWall_Area_2,\
    ProofExport_Area_2,HorizontalFlueSideWall_Area_2,\
    RearShaftWallTube38_Area_2,RearShaftWallTube51_Area_2, \
    LowTemperatureSuperheater_Area_2,PlatenSuperheater45_Area_2, \
    PlatenSuperheater51_Area_2,HighTemperatureSuperheater45_Area_2, \
    HighTemperatureSuperheater51_Area_2,HighTemperatureReheater_Area_2,\
    LowTemperatureReheater_Area_2


from Monitor.utils.brokenLineFuntion import\
    economizerExportFunc,proofExportFunc\
    ,horizontalFlueSideWalltFunc \
    ,rearShaftWallTubeModle38Func,\
    rearShaftWallTubeModle51Func,lowTemperatureSuperheaterFunc,\
    platenSuperheaterModle45Func,platenSuperheaterModle51Func,\
    highTemperatureSuperheaterFunc45,highTemperatureSuperheaterFunc51,\
    highTemperatureReheaterFunc,lowTemperatureReheaterFunc







#定时工作
def schGrqTask():

    #省煤器区域温度数据监控
    # temperatureMonitorHandle(15,economizerExportFunc,OPC_DATA_CLASSIFICATION_GRQ)
    # 顶棚区域温度数据监控
    temperatureMonitorHandle(25, proofExportFunc, ProofExport_Area_2)
    # 水平烟道侧包墙区域温度数据监控
    temperatureMonitorHandle(20, horizontalFlueSideWalltFunc, HorizontalFlueSideWall_Area_2)
    # 后竖井包墙管38区域温度数据监控
    temperatureMonitorHandle(23, rearShaftWallTubeModle38Func, RearShaftWallTube38_Area_2)
    # 后竖井包墙管51区域温度数据监控
    temperatureMonitorHandle(23, rearShaftWallTubeModle51Func, RearShaftWallTube51_Area_2)
    # 低温过热器区域温度数据监控
    temperatureMonitorHandle(16.5, lowTemperatureSuperheaterFunc, LowTemperatureSuperheater_Area_2)
    # 屏式过热器45域温度数据监控
    temperatureMonitorHandle(20, platenSuperheaterModle45Func, PlatenSuperheater45_Area_2)
    # 屏式过热器51区域温度数据监控
    temperatureMonitorHandle(21, platenSuperheaterModle51Func, PlatenSuperheater51_Area_2)
    # 高温过热器45出口区域温度数据监控
    temperatureMonitorHandle(19, highTemperatureSuperheaterFunc45, HighTemperatureSuperheater45_Area_2)
    # 高温过热器51出口区域温度数据监控
    temperatureMonitorHandle(19, highTemperatureSuperheaterFunc51, HighTemperatureSuperheater51_Area_2)
    # 高温再热器区域温度数据监控
    temperatureMonitorHandle(4.3, highTemperatureReheaterFunc, HighTemperatureReheater_Area_2)
    # 低温再热器区域温度数据监控
    temperatureMonitorHandle(4.3, lowTemperatureReheaterFunc, LowTemperatureReheater_Area_2)









#定时任务配置

def run_task():

    try:
        # 实例化调度器
        scheduler = BackgroundScheduler()
        # 调度器使用DjangoJobStore()
        # scheduler.add_jobstore(DjangoJobStore(), "default")
        # 使用IntervalTrigger指定时间运行
        scheduler.add_job(schGrqTask, 'interval',seconds=SCHEDULER_INTERVAL)
        scheduler.start()
    except(KeyboardInterrupt,SystemExit):
        scheduler.shutdown()

