from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item
from django.contrib.auth.models import User
from bid.forms.bid_forms import BidForm
from item.views import get_item_by_id

# Create your views here.


def make_bid(request, id):
    item = get_object_or_404(Item, pk=id)
    item.highest_bid
    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            if bid.bid_amount >= item.highest_bid * 1.05:
                bid.bidder = request.user
                bid.item_id = item.id
                bid.save()
                messages.success(request,
                                 f"Your bid of ${bid.bid_amount} for Item: {item.name}, has been successfully placed!")
                item.highest_bid = bid.bid_amount
                item.save()
                return redirect("item-index")
            else:
                messages.error(request,f"Minimum bid amount is {item.highest_bid * 1.05}")
                return redirect("make_bid", id=id)


    bid = BidForm()

    context = {
        "form": bid,
        "item": item,
    }
    return render(request, "bid/make_bid.html", context)
