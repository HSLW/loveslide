from rest_framework import viewsets
from lockscreen.models import Card
from lockscreen.serializers import CardSerializer


class CardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer