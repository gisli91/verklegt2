from django.db import models
from item.models import Item
from django.contrib.auth.models import User
from datetime import datetime


class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    bid_amount = models.FloatField()
    bid_posted = models.DateTimeField(default=datetime.now(), blank=True)
    bid_accepted = models.BooleanField(default=False)


