from rest_framework import serializers
from .models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    follower = serializers.StringRelatedField(many=True, read_only=True)
    following = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('avatar', 'baio', 'follower', 'following', 'created')