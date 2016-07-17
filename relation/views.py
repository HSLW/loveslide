from django.shortcuts import render
from relation.models import Like
from relation.serializers import LikeSerializer
from rest_framework import generics
from rest_framework import viewsets


class LikeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
