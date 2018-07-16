from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import mixins, viewsets

from video1.models import Video
from video1.serializers import VideoSerializer


def index(request):
    return HttpResponse('走错了')


class IndexViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
