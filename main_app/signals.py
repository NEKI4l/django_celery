from django.db.models.signals import post_save
from main_app.models import User
from main_app.tasks import send_verification_email
from django.dispatch import receiver


@receiver(post_save, sender=User)
def user_update(sender, instance, *args, **kwargs):
    if not instance.is_verified:
        send_verification_email.delay(instance.pk)