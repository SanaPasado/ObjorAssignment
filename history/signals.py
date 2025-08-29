# your_app_name/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tweet, History

@receiver(post_save, sender=Tweet)
def create_history_on_tweet_save(sender, instance, created, **kwargs):

    if created:
        History.objects.create(
            user=instance.user,
            method="POST",
            tweet=instance,
            summary=f"User {instance.user} created a tweet with content: '{instance.content}' at '{instance.created_at}'"
        )


