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
                                                 'video_url': 'http://www.iqiyi.com/v_19rrbooge4.html'})


class IndexViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    # permission_classes = [BaseOperatePermission]
