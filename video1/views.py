from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import mixins, viewsets

from permissions.base_permissions import BaseOperatePermission
from video1.models import Video
from video1.serializers import VideoSerializer

from django.shortcuts import render_to_response

def index(request):
    return render(request, 'index.html')


class IndexViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    # permission_classes = [BaseOperatePermission]
