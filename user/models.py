from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from item.models import Item


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)