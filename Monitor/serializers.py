#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/5 14:23'

from django.contrib.auth.models import User
from rest_framework import  serializers, viewsets
from .models import Snippet,Opcitemrtvalue


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id','title', 'code', 'linenos', 'language', 'style')


class OpcRealTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcitemrtvalue
        fields = ('name','itemid', 'value', 'groupname')