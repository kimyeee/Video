from rest_framework import routers
from video.views import IndexViewSet

router = routers.SimpleRouter()
router.register(r'a', IndexViewSet)

urlpatterns = router.urls

