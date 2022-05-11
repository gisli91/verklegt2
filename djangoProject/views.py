from item.models import Item
from django.shortcuts import render


def frontpage(request):
    newest_items = Item.objects.all().order_by("date_posted")
    return render(request, "frontpage.html",{
        "newest_items": newest_items
    })