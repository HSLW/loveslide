from rest_framework.decorators import list_route
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from relation.models import Like
from relation.serializers import LikeSerializer
from rest_framework import viewsets

import logging

logger = logging.getLogger(__name__)


class LikeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def retrieve(self, request, pk=None):
        queryset = Like.objects.all().filter(user2=pk)
        serializer = LikeSerializer(queryset)
        return Response(serializer.data)


class CardViewSet(object):
    pass