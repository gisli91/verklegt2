from datetime import datetime
from PIL import Image
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    highest_bid = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=datetime.now(), blank=True)
    item_image = models.ImageField(default="default-item.jpg", upload_to="item_images")

    def save(self):
        super().save()

        img = Image.open(self.item_image.path)
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.item_image.path)







