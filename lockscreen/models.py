from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Card(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=1000)
    age = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    region = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    message = models.CharField(max_length=255)
