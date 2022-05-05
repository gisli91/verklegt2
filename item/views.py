from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from item.forms.item_form import ItemCreateForm
from item.models import Item, ItemImage


# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {"items": Item.objects.all().order_by("name")}
    return render(request, "item/index.html", context)


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



