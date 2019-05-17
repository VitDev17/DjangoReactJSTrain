from rest_framework import routers
from .api import HallNewsViewset

router = routers.DefaultRouter()
router.register('api/HallNews',HallNewsViewset,'HallNews')

urlpatterns = router.urls