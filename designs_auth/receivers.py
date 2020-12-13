from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from designs_auth.models import UserProfile


@receiver(post_save, sender=User)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        profile = UserProfile(
            user=instance,
            # profile_picture=instance.profile_picture,
            # facebook=instance.facebook,
            # twitter=instance.twitter,
            # instagram=instance.instagram,
            # portfolio=instance.portfolio,

        )
        profile.save()
