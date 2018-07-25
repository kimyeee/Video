from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import mixins, viewsets

from permissions.base_permissions import BaseOperatePermission
from video1.models import Video
from video1.serializers import VideoSerializer

from django.shortcuts import render_to_response


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def detail(request):
    return render(request, 'video_detail.html', {'title': '我不是药神',
                                                 'video_url': 'https://v.youku.com/v_show/id_XMzY0NzIwODI3Ng==.html?spm=a2h03.8173536.2100006.8'})


class IndexViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    # permission_classes = [BaseOperatePermission]
