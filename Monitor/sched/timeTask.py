from apscheduler.schedulers.background import BackgroundScheduler
from Monitor.sched.TempratureHandle import economizerExportHandle
from datetime import datetime





#处理过热器数据，并保存
def schGrqTask():

    economizerExportHandle(15)







#定时任务配置

def run_task():

    try:
        # 实例化调度器
        scheduler = BackgroundScheduler()
        # 调度器使用DjangoJobStore()
        # scheduler.add_jobstore(DjangoJobStore(), "default")
        # 使用IntervalTrigger指定时间运行
        scheduler.add_job(schGrqTask, 'interval',seconds=5)
        scheduler.start()
    except(KeyboardInterrupt,SystemExit):
        scheduler.shutdown()

