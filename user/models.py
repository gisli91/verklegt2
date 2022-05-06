from django.contrib.auth.models import User
from django.db import models
from item.models import Item
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(default="default.jpg", upload_to="profile_images")


    def __str__(self):
        return f"{self.user.username} Profile"