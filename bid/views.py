from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item
from django.contrib.auth.models import User
from bid.forms.bid_forms import BidForm
from message.models import Message

# Create your views here.
from bid.models import Bid
from payment.forms.payment_form import PaymentForm
from payment.models import Payment


@login_required
def accept_bid(request, id):
    bid = get_object_or_404(Bid, pk=id)
    content = f"Your bid for ${bid.bid_amount} for item {bid.item} from user {bid.bidder}"
    header = f"Your bid for  {bid.item.name} has been accepted!"
    sender = User.objects.filter(username="Notifications").first()
    Message.objects.create(message_content=content,
                           subject_header=header,
                           sender=sender,
                           receiver=bid.bidder,
                           is_bid=True,
                           bid_id=bid,
                           is_bid_accepted=True)

    return redirect(f"/messages/")


@login_required
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
                messages.error(request, f"Minimum bid amount is {item.highest_bid * 1.05}")
                return redirect("make_bid", id=id)

    bid = BidForm()

    context = {
        "form": bid,
        "item": item,
    }
    return render(request, "bid/make_bid.html", context)
