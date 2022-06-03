from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'post', 'user', 'text')

    
class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    
    tags = TagListSerializerField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('pk', 'title', 'description', 'image', 'tags', 'comments', 'created')


