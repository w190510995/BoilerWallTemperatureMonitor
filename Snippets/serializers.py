#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2018/12/5 14:02'

from rest_framework import serializers
from Snippets.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id','title', 'code', 'linenos', 'language', 'style')
