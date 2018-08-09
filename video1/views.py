import time
from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.decorators import detail_route, list_route

from permissions.base_permissions import BaseOperatePermission
from video1.models import Video, SpiderVideo, VideoClass
from video1.serializers import VideoSerializer, SpiderVideoSerializer, VideoClassSerializer

from django.shortcuts import render_to_response

from .spider import Spider


def v_index(request):
    return render(request, 'video/index2.html')


def home(request):
    return render(request, 'init.html')


def filter(request):
    return render(request, 'filter.html')


def search(request):
    print(request.content_params)
    return render(request, 'movie/search.html', {'title': '我不是药神'})


def detail(request):
    a= 11
    print(111)
    return render(request, 'detail.html', {'title': '我不1是药神',
                                           'video_url': 'http://www.iqiyi.com/v_19rrbooge4.html'})


class VideoViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    # permission_classes = [BaseOperatePermission]


class VideoClassViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = VideoClass.objects.all()
    serializer_class = VideoClassSerializer
    # permission_classes = [BaseOperatePermission]


class SpiderVideoViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    queryset = SpiderVideo.objects.all()
    serializer_class = SpiderVideoSerializer

    # permission_classes = [BaseOperatePermission]

    @list_route()
    def get_movie(self, request):
        Spider.get_youku_movie()

        # Spider.get_aiqiyi_movie()
        #
        # Spider.get_tencent_movie()
        return HttpResponse('ok')

    @list_route()
    def online(self, request):
        Video.objects.bulk_create(SpiderVideo.objects.all())
        return HttpResponse('ok')
