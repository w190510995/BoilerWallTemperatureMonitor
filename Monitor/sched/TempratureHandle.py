#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/24 13:54'
from django.core.cache  import cache
from datetime import  datetime
from ..config import OPC_REAL_DATA_API,\
    OPC_DATA_CLASSIFICATION_GRQ,OPC_DATA_CLASSIFICATION_HQ,\
    OPC_DATA_CLASSIFICATION_OHTER,OPC_DATA_CLASSIFICATION_QQ,\
    OPC_DATA_CLASSIFICATION_ZRQ,OPC_DATA_CLASSIFICATION_BSGR,\
    OPC_DATA_CLASSIFICATION_DLGR
import logging,requests
import pandas as pd
from Monitor.models import TempratureAlermValue
from Monitor.utils.timpratureTools import dataProcess
from Monitor.utils.brokenLineFuntion import\
    economizerExportFunc,horizontalFlueSideWalltFunc \
    ,proofExportFunc,rearShaftWallTubeModle38Func,\
    rearShaftWallTubeModle51Func,lowTemperatureSuperheaterFunc,\
    platenSuperheaterModle45Func,platenSuperheaterModle51Func,\
    highTemperatureSuperheaterFunc45,highTemperatureSuperheaterFunc51,\
    highTemperatureReheaterFunc,lowTemperatureReheaterFunc

data_url = OPC_REAL_DATA_API

#从OPC接口软件中获取数据,并拿出指定区域的数据
def getUrlDataHandle(url,area):
    try:
        opc_real_data = requests.get(url).json()  # 获取OPC_API 接口软件实时数据
        pd_opc_real_data = pd.DataFrame(opc_real_data)  # 转为pandas的DataFrame数据格式，以便处理
        pd_condition_data = pd_opc_real_data[pd_opc_real_data['GroupName'] == area]  # 获取指定区域的数据
    except:
        logging.error('从OPC接口软件获取 API 数据失败（api_views.py   opc_area_Procesed）')
    return pd_condition_data

#生成报警阈值
def createAlarmThreshold(value,modle):
    return modle(value)





def economizerExportHandle(pressure):

    #生成报警定值
    thresholdValuet = economizerExportFunc(pressure)

    #获取opc数据
    opc_client_api_data = getUrlDataHandle(data_url,OPC_DATA_CLASSIFICATION_GRQ)
    pd_filter_data = opc_client_api_data[['Name','Value']]  # 获取指定字段的数据
    # print(pd_filter_data)
    for index,row in pd_filter_data.iterrows():

        tagName = row['Name']
        tagValue = round(float(row['Value']),2)
        dataProcess(tagName,tagValue,thresholdValuet,OPC_DATA_CLASSIFICATION_GRQ)



