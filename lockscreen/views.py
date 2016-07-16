from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from lockscreen.models import Card
from lockscreen.serializers import CardSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer