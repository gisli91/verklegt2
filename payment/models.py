from django.db import models
from item.models import Item
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
from bid.models import Bid


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    card_nr = models.IntegerField(blank=True, null=True)
    cvc_nr = models.IntegerField(blank=True, null=True)
    exp_date = models.IntegerField(blank=True, null=True)

