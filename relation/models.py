from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Like(models.Model):
    user1 = models.ForeignKey(User, related_name='user1')
    user2 = models.ForeignKey(User, related_name='user2')
    liked_at = models.DateTimeField(auto_now_add=True)
