from rest_framework.decorators import list_route
from rest_framework.response import Response

from relation.models import Like
from relation.serializers import LikeSerializer
from rest_framework import viewsets

import logging

logger = logging.getLogger(__name__)


class LikeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    @list_route()
    def recent_users(self, request):
        logger.info(request)
        recent_users = Like.objects.filter(user2=1)

        serializer = self.get_serializer(recent_users)
        return Response(serializer.data)


class CardViewSet(object):
    pass