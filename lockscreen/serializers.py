from lockscreen.models import Card
from rest_framework import serializers


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('name', 'image_url', 'age', 'height', 'job', 'region', 'message')
