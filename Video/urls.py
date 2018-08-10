"""Video URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from movie.views import index, home, detail, search, video_filter, video_play
from video1.views import v_index

urlpatterns = [
    url(r'^api/', include('video1.urls')),
    url(r'movie', home),
    url(r'video_detail/(.+)/$', detail),
    url(r'video_play/(.+)/$', video_play),
    url(r'search', search),
    url(r'filter', video_filter),
    url(r'index2/', v_index),
    url(r'^$', index),
]
