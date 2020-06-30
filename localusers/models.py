from django.contrib.auth.models import AbstractUser
from django.db import models


class LocalUser(AbstractUser):
    money = models.IntegerField('Money', default=0, blank=True)
