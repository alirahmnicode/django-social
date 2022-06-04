from rest_framework import serializers
from .models import Profile

class ProfileSerializers(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    follower = serializers.StringRelatedField(many=True, read_only=True)
    following = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'avatar', 'baio', 'follower', 'following', 'created')