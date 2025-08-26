from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import settings
from tweets.models import Tweet

class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    method = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    summary = models.TextField()


    def __str__(self):
        return self.summary[:50]