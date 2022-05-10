from django.contrib.auth.models import User
from django.db import models
from item.models import Item
from PIL import Image
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(default="default.jpg", upload_to="profile_images")


    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        super().save()

        img = Image.open(self.profile_image.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)

