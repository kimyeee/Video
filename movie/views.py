import time
from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import mixins, viewsets

from permissions.base_permissions import BaseOperatePermission
from video1.models import Video
from video1.serializers import VideoSerializer

from django.shortcuts import render_to_response


# c = 0
# s = time.time()
# obj = Video.objects.filter(name='wo')
# global c
# global s
#
# if c % 100 == 0:
#     print(time.time() - s)
#     print('+' * 60, c)
# c += 1

def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'init.html')

def filter(request):
    return render(request, 'filter.html')


def search(request):
    print(request.content_params)
    return render(request, 'search.html', {'title': '我不是药神'})


def detail(request):
    return render(request, 'detail.html', {'title': '我不是药神',
                                           'video_url': 'http://www.iqiyi.com/v_19rrbooge4.html'})


class IndexViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    # permission_classes = [BaseOperatePermission]