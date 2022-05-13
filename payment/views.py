from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Create your views here.
from bid.models import Bid
from payment.forms.payment_form import PaymentForm


def payment_screen(request, id):
    bid = get_object_or_404(Bid, pk=id)
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = bid.bidder
            payment.bid = bid
            payment.save()
            item = payment.bid.item
            item.item_listed = False
            item.save()
            messages.success(request, f"Your, payment was successful!")

    payment = PaymentForm()

    context = {
        "form": payment,
        "id": id
    }

    return render(request, "payment/single_payment.html", context)
