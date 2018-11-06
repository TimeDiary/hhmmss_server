from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    name = models.CharField(max_length=100, blank=True, null=True)


class CustomUser(AbstractUser):
    objects = CustomUserManager()
