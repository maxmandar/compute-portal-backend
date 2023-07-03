from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Custom User'




class CustomGroup(Group):
    active = models.BooleanField(default=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Custom Group'