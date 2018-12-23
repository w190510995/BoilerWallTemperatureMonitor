from apscheduler.schedulers.background import BackgroundScheduler
import logging,requests,datetime
import pandas as pd
from ..models import GrqMeanValue
from ..config import OPC_REAL_DATA_API,\
    OPC_DATA_CLASSIFICATION_GRQ,OPC_DATA_CLASSIFICATION_HQ,\
    OPC_DATA_CLASSIFICATION_OHTER,OPC_DATA_CLASSIFICATION_QQ,\
    OPC_DATA_CLASSIFICATION_ZRQ,OPC_DATA_CLASSIFICATION_BSGR,\
    OPC_DATA_CLASSIFICATION_DLGR

#处理过热器数据，并保存
def schGrqTask():

    print('schGrqTask>>>' ,datetime.datetime.now()) #定时任务

    url = OPC_REAL_DATA_API

    try:
        opc_real_data = requests.get(url).json()  # 获取OPC_API 接口软件实时数据
    except:
        logging.error('获取OPC API 数据失败（api_views.py   opc_area_Procesed）')

    pd_opc_real_data = pd.DataFrame(opc_real_data)  # 转为pandas的DataFrame数据格式，以便处理
    pd_condition_data = pd_opc_real_data[pd_opc_real_data['GroupName'] == OPC_DATA_CLASSIFICATION_GRQ]

    pd_filter_data = pd_condition_data[['Value']]  # 获取指定字段的数据

    # pd_value_mean = pd_filter_data.mean()
    # temp_data = GrqMeanValue(area=OPC_DATA_CLASSIFICATION_GRQ, value=int(pd_value_mean),created=datetime.datetime.now())
    # temp_data.save()








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

