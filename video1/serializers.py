# coding: utf-8
import datetime

from rest_framework import serializers

import logging

from .models import Video, SpiderVideo

logger = logging.getLogger('django')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'v_class', 'name', 'cover', 'online_time', 'actor', 'region', 'tags', 'video_url', 'summarize',
                  'create_time']


class SpiderVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpiderVideo
        fields = ['id', 'v_class', 'name', 'cover', 'online_time', 'actor', 'region', 'tags', 'video_url', 'summarize',
                  'create_time']

# class VideoDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VideoDetail
#         fields = ['openid']


# class TagsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tags
#         fields = ['name']
