from django.forms import ModelForm, widgets
from django import forms

from item.models import Item


class ItemUpdateForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "description", "highest_bid", "item_image", "category"]



class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "description", "highest_bid", "item_image", "category"]
