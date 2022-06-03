from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from user.permissions import ObjectOwner
from .serializers import PostSerializer, CommentSerializer
from .permissions import CommentAccesse
from .models import Post, Comment


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [ObjectOwner]

    def perform_create(self, serializer):
        user = None
        if self.request and hasattr(self.request, "user"):
            user = self.request.user
            serializer.save(user=user)

    def get_queryset(self):
        return Post.objects.all()

    
class CommentViewSet(ListModelMixin, DestroyModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, CommentAccesse]
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        user = None
        if self.request and hasattr(self.request, "user"):
            user = self.request.user
            serializer.save(user=user)
