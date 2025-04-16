from django.conf import settings
from django.db import models
from django.utils import timezone

#WE WILL NEED:
# a class for lost pets and found pets OR a pets class that has lost/found 
# statuses that we can use to decide what goes where

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title