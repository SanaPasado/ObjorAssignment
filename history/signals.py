from django.db.models.signals import post_save
from django.dispatch import receiver
from tweets.models import Tweet
from .models import History

@receiver(post_save, sender=Tweet)
def create_history_on_tweet(sender, instance, created, **kwargs):
    if created:
        History.objects.create(
            user=instance.user,
            method="POST",
            tweet=instance,  # ✅ this matches the FK now
            summary=f"User {instance.user.username} created tweet with a content of '{instance.content}' at {instance.created_at}"
        )

