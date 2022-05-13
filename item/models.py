from datetime import datetime
from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.



class Item(models.Model):
    CATEGORY_CHOICE = (
        ("Furniture", "Furniture"),
        ("Appliances", "Appliances"),
        ("Electronics", "Electronics"),
        ("Computers", "Computers"),
        ("Pets", "Pets"),
        ("Men's Clothing", "Mens Clothing"),
        ("Women's Clothing", "Womens Clothing"),
        ("Vehicles", "Vehicles"),
        ("Cars", "Cars"),
        ("Bikes", "Bikes"),
        ("Instruments", "Instruments"),
        ("Toys", "Toys"),
        ("Books", "Books"),
        ("Tools", "Tools"),
        ("Other", "Other")


    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    highest_bid = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=datetime.now(), blank=True)
    item_image = models.ImageField(default="default-item.jpg", upload_to="item_images")
    category = MultiSelectField(choices=CATEGORY_CHOICE, null=True)
    item_listed = models.BooleanField(default=True)

    def __str__(self):
        return self.name







    def save(self):
        super().save()

        img = Image.open(self.item_image.path)
        output_size = (400, 400)
        img.thumbnail(output_size)
        img.save(self.item_image.path)
