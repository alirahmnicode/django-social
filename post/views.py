from rest_framework import viewsets
from user.permissions import ObjectOwner
from .serializers import PostSerializer
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [ObjectOwner]

    def perform_create(self, serializer):
        user = None
        if self.request and hasattr(self.request, "user"):
            user = self.request.user
            serializer.save(user=user)

    def get_queryset(self):
        return Post.objects.all()

    
