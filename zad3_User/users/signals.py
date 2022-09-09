import datetime

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import User
from django.contrib.auth.signals import user_login_failed


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         User.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
#
#
# @receiver(user_login_failed)
# def save_date_login_failed(sender, credentials, request, **kwargs):
#     user_name = credentials['username']
#
#     if User.objects.filter(username=user_name).exists():
#         user_object = User.objects.get(username=user_name)
#         profile_object = Profile.objects.get(id=user_object.id)
#
#         profile_object.last_login_failed = datetime.datetime.now()
#         profile_object.save()
