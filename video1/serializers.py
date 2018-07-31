# coding: utf-8
import datetime

from rest_framework import serializers

import logging

from .models import Video

logger = logging.getLogger('django')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id','name', 'cover', 'actor', 'type', 'summarize']


# class VideoDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VideoDetail
#         fields = ['openid']


# class TagsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tags
#         fields = ['name']
