from rest_framework import routers
from movie.views import IndexViewSet

router = routers.SimpleRouter()
router.register(r'a', IndexViewSet)

urlpatterns = router.urls

