from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField
from .models import Post


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    
    tags = TagListSerializerField(read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'description', 'image', 'tags', 'created')