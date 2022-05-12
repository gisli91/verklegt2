from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from item.forms.item_form import ItemCreateForm, ItemUpdateForm
from item.models import Item


# Create your views here.
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    if "search_filter" in request.GET:
        search_filter = request.GET["search_filter"]
        items = [{
            "id": x.id,
            "name": x.name,
            "seller": x.seller.username,
            "highest_bid": x.highest_bid,
            "category": x.category,
            "image": x.item_image.url
        } for x in Item.objects.filter(name__icontains=search_filter)]
        return JsonResponse({"data": items})

    elif "sort_name_filter" in request.GET:
        sort_name_filter = request.GET["sort_name_filter"]
        items = [{
            "id": x.id,
            "name": x.name,
            "seller": x.seller.username,
            "highest_bid": x.highest_bid,
            "category": x.category,
            "image": x.item_image.url
        } for x in Item.objects.all().order_by("name")]
        return JsonResponse({"data": items})

    elif "sort_price_filter" in request.GET:
        items = [{
            "id": x.id,
            "name": x.name,
            "seller": x.seller.username,
            "highest_bid": x.highest_bid,
            "category": x.category,
            "image": x.item_image.url
        } for x in Item.objects.all().order_by("highest_bid")]
        return JsonResponse({"data": items})

    context = {"items": Item.objects.all().order_by("name")}
    return render(request, "item/index.html", context)


@login_required
def auction_item(request):
    if request.method == "POST":
        form = ItemCreateForm(request.POST, request.FILES)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.seller = request.user
            auction.save()
            return redirect("item-index")
    form = ItemCreateForm()
    return render(request, "item/auction_item.html", {
        "form": form
    })

def get_item_by_id(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, "item/item-details.html", {
        "item": item,
        "related_items": Item.objects.filter(Q(category=item.category) | Q(seller=item.seller)).exclude(id=item.id)
    })

@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    if item.seller == request.user:
        item.delete()
    return redirect("item-index")


@login_required
def update_item(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        form = ItemUpdateForm(data=request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item_details", id=id)
    else:
        form = ItemUpdateForm(instance=item)
    return render(request, "item/update_item.html", {
        "form": form,
        "id": id
    })



