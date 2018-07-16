from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets

from video.models import Video
from video.serializers import VideoSerializer


class IndexViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
