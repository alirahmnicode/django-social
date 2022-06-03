from django.urls import path
from rest_framework import routers
from .views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('post', PostViewSet, basename='post')
router.register('comments', CommentViewSet)

urlpatterns = router.urls