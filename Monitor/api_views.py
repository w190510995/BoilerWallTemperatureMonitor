#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/5 14:26'

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status



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




@api_view(['GET', 'POST'])
def opc_real_list(request,format=None):
    if request.method == 'GET':
        data_list = Opcitemrtvalue.objects.all()
        serializer = OpcRealTimeSerializer(data_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OpcRealTimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
