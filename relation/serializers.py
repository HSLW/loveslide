from rest_framework import serializers
from relation.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user1', 'user2', 'liked_at')
