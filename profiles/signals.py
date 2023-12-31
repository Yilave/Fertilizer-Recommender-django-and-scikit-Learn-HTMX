from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import Profile
from django.dispatch import receiver 
User = get_user_model()


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)