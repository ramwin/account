"""
django custome auth model
"""


from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """customer User"""
    name = models.CharField(max_length=31, blank=True)
    phone_number = models.CharField(max_length=31, blank=True)
