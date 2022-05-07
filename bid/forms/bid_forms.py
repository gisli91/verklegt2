from django import forms
from django.core.exceptions import ValidationError

from item.models import Item
from bid.models import Bid


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ["bid_amount"]

