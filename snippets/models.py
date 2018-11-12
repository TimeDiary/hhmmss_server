from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    owner = models.ForeignKey(User, related_name='locations', on_delete=models.CASCADE)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    retrieved = models.BooleanField()

    class Meta:
        ordering = ('created',)
