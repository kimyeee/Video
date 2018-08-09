from rest_framework import routers
from video1.views import VideoViewSet, SpiderVideoViewSet, VideoClassViewSet

router = routers.SimpleRouter()
router.register(r'video', VideoViewSet)
router.register(r'video_class', VideoClassViewSet)
router.register(r'spider_video', SpiderVideoViewSet)

urlpatterns = router.urls

