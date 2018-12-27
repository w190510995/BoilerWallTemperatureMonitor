
from apscheduler.schedulers.background import BackgroundScheduler
from Monitor.sched.TempratureHandle import temperatureMonitorHandle


from ..config import   OPC_DATA_CLASSIFICATION_GRQ,SCHEDULER_INTERVAL\
    ,OPC_DATA_CLASSIFICATION_HQ,\
    OPC_DATA_CLASSIFICATION_OHTER,OPC_DATA_CLASSIFICATION_QQ,\
    OPC_DATA_CLASSIFICATION_ZRQ,OPC_DATA_CLASSIFICATION_BSGR,\
    OPC_DATA_CLASSIFICATION_DLGR
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
    temperatureMonitorHandle(15,economizerExportFunc,OPC_DATA_CLASSIFICATION_GRQ)
    # 顶棚区域温度数据监控
    temperatureMonitorHandle(15, proofExportFunc, OPC_DATA_CLASSIFICATION_HQ)
    # 水平烟道侧包墙区域温度数据监控
    temperatureMonitorHandle(15, horizontalFlueSideWalltFunc, OPC_DATA_CLASSIFICATION_OHTER)
    # 后竖井包墙管38区域温度数据监控
    temperatureMonitorHandle(15, rearShaftWallTubeModle38Func, OPC_DATA_CLASSIFICATION_GRQ)
    # 后竖井包墙管51区域温度数据监控
    temperatureMonitorHandle(15, rearShaftWallTubeModle51Func, OPC_DATA_CLASSIFICATION_ZRQ)
    # 低温过热器区域温度数据监控
    temperatureMonitorHandle(15, lowTemperatureSuperheaterFunc, OPC_DATA_CLASSIFICATION_QQ)
    # 屏式过热器45域温度数据监控
    temperatureMonitorHandle(15, platenSuperheaterModle45Func, OPC_DATA_CLASSIFICATION_BSGR)
    # 屏式过热器51区域温度数据监控
    temperatureMonitorHandle(15, platenSuperheaterModle51Func, OPC_DATA_CLASSIFICATION_GRQ)
    # 高温过热器45出口区域温度数据监控
    temperatureMonitorHandle(15, highTemperatureSuperheaterFunc45, OPC_DATA_CLASSIFICATION_QQ)
    # 高温过热器51出口区域温度数据监控
    temperatureMonitorHandle(15, highTemperatureSuperheaterFunc51, OPC_DATA_CLASSIFICATION_QQ)
    # 低温再热器区域温度数据监控
    temperatureMonitorHandle(15, lowTemperatureReheaterFunc, OPC_DATA_CLASSIFICATION_DLGR)
    # 高温再热器区域温度数据监控
    temperatureMonitorHandle(15, highTemperatureReheaterFunc, OPC_DATA_CLASSIFICATION_OHTER)







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

