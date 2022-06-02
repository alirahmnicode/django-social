from rest_framework import routers
from .views import PostViewSet

router = routers.DefaultRouter()
router.register('post', PostViewSet, basename='post')
urlpatterns = router.urls