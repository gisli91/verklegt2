from django.db import models
from item.models import Item
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from datetime import datetime
# Create your models here.
from bid.models import Bid


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    country = CountryField(blank=True, null=True)
    card_nr = models.IntegerField(blank=True, null=True)
    cvc_nr = models.IntegerField(blank=True, null=True)
    exp_date = models.IntegerField(blank=True, null=True)
    is_processed = models.BooleanField(default=False)

