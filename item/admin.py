from django.contrib import admin

from .forms.item_form import *
from .models import *


# Register your models here.



@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    form = ItemCreateForm
