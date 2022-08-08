from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.conf import settings
from django.core.mail import send_mail
from .models import Profile


def emailMessages(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.get(user=user)
        subject = 'Welcome to "To Do List" app'
        message = 'We are glad that you are here!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if not created:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


post_save.connect(updateUser, sender=Profile)