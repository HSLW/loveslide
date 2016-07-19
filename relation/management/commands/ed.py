from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from relation.models import Like


class Command(BaseCommand):
    def handle(self, *args, **options):
        user1 = User.objects.filter(id=1)
        user2 = User.objects.filter(id=2)
        user3 = User.objects.filter(id=3)
        like1 = Like.objects.create(user1=user1, user2=user2)
        like2 = Like.objects.create(user1=user3, user2=user2)
        like3 = Like.objects.create(user1=user2, user2=user1)
        like1.save()
        like2.save()
        like3.save()
