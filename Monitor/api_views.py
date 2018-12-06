#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/5 14:26'

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from . import config
import requests
import pandas as pd




from .models import Opcitemrtvalue
from .serializers import  OpcRealTimeSerializer

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class OpcRealTimeViewSet(viewsets.ModelViewSet):
#     queryset = Opcitemrtvalue.objects.all()
#     serializer_class = OpcRealTimeSerializer
#






@api_view([ 'POST'])
def opc_real_list(request,format=None):
    condition = request.POST['condition']

    try:
        data_list = Opcitemrtvalue.objects.filter(groupname__exact=condition)
        serializer = OpcRealTimeSerializer(data_list, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view([ 'POST'])
def opc_area_Procesed(request,format=None):

    url = config.OPC_REAL_DATA_API
    condition = request.POST['condition']

    opc_real_data = requests.get(url).json() #获取OPC_API 接口软件实时数据
    pd_opc_real_data = pd.DataFrame(opc_real_data) #转为pandas的DataFrame数据格式，以便处理

    pd_condition_data =  pd_opc_real_data[pd_opc_real_data['GroupName'] == condition]
    # pd_filter_data =  pd_condition_data.drop(columns=['Access','Code','Status','DataType','Timestamp','ServerName',
    #                                'Status','Timestamp','ItemID'],
    #                       axis=1,inplace=True)  #删除不需要的列
    pd_filter_data = pd_condition_data[['Name','Value','GroupName']] #获取指定字段的数据

    print(pd_filter_data)

    try:
        data_list = Opcitemrtvalue.objects.filter(groupname__exact=condition)
        serializer = OpcRealTimeSerializer(data_list, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# @api_view(['GET', 'POST'])
# def opc_real_list(request,format=None):
#     if request.method == 'GET':
#         data_list = Opcitemrtvalue.objects.all()
#         serializer = OpcRealTimeSerializer(data_list, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         data_list = Opcitemrtvalue.objects.all()
#         serializer = OpcRealTimeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)