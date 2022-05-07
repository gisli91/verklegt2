from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item
from django.contrib.auth.models import User
from bid.forms.bid_forms import BidForm

# Create your views here.



def make_bid(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.item = item
            bid.bidder = request.user
            bid.save()
            return redirect("item-index")
    else:
        bid = BidForm()

    context = {
        "form": bid,
        "item": item,
    }
    return render(request, "bid/make_bid.html", context)
