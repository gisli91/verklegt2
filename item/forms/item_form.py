from django.forms import ModelForm, widgets
from django import forms

from item.models import Item


class ItemUpdateForm(ModelForm):
    class Meta:
        model = Item
        exclude = ["id", "seller", "date_posted"]
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control"}),
            "description": widgets.TextInput(attrs={"class": "form-control"}),
            "category": widgets.Select(attrs={"class": "form-control"}),
            "price": widgets.NumberInput(attrs={"class": "form-control"}),
        }


class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "description", "highest_bid", "item_image", "category"]
