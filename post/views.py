from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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


class LikeView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def post(self, request, **kwargs):
        user = request.user
        post = get_object_or_404(Post, pk=kwargs['pk'])

        if user in post.like.all():
            # unlike
            post.like.remove(user)
            post.save()
            return Response('The post is unliked.', status=status.HTTP_200_OK)
        else:
            # like
            post.like.add(user)
            post.save()
            return Response('The post is liked.', status=status.HTTP_200_OK)

        
