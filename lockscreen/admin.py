from django.contrib import admin
from lockscreen.models import Card
from relation.models import Like
# Register your models here.

admin.site.register(Card)
admin.site.register(Like)
