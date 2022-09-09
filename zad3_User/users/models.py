from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)tdj
    last_login_failed = models.DateTimeField(null=True, blank=True)
    bio = models.TextField(max_length=1000, blank=True)

