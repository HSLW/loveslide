from django.core.management.base import BaseCommand
from relation.models import Like


class Command(BaseCommand):
    def handle(self, *args, **options):
        like1 = Like.objects.create(user1=2, user2=1)
        like2 = Like.objects.create(user1=3, user2=1)
        like3 = Like.objects.create(user1=4, user2=1)
        like1.save()
        like2.save()
        like3.save()