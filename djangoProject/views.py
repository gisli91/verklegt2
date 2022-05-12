from item.models import Item
from django.shortcuts import render


def frontpage(request):
    latest_items = [{
        "id": x.id,
        "name": x.name,
        "seller": x.seller.username,
        "highest_bid": x.highest_bid,
        "category": x.category,
        "item_image_url": x.item_image.url
    } for x in Item.objects.all().order_by("-date_posted")]
    return render(request, "frontpage.html",{
        "newest_items": latest_items[:3]
    })