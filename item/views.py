from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from item.forms.item_form import ItemCreateForm
from item.models import Item, ItemImage


# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {"items": Item.objects.all().order_by("name")}
    return render(request, "item/index.html", context)

def frontpage(request):
    return render(request, "frontpage.html")


@login_required
def auction_item(request):
    if request.method == "POST":
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.seller = request.user
            auction.save()
            item_img = ItemImage(image=request.POST["image"], item=auction)
            item_img.save()
            return redirect("item-index")
    form = ItemCreateForm()
    return render(request, "item/auction_item.html", {
        "form": form
    })

def get_item_by_id(request, id):
    return render(request, "item/item-details.html", {
        "item": get_object_or_404(Item, pk=id)
    })

@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    if item.seller == request.user:
        item.delete()
    return redirect("item-index")

