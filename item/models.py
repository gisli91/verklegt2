from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    highest_bid = models.FloatField()
    # seller = models.ForeignKey(User, on_delete=models.CASCADE)

class ItemImage(models.Model):
    image = models.CharField(max_length=9999)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)



