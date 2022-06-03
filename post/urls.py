from django.urls import path
from rest_framework import routers
from .views import PostViewSet, CommentViewSet, LikeView

router = routers.DefaultRouter()
router.register('post', PostViewSet, basename='post')
router.register('comments', CommentViewSet)

urlpatterns = [
    path('post/<int:pk>/like-unlike/', LikeView.as_view())
]

urlpatterns += router.urls