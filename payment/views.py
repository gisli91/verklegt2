from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from bid.models import Bid
from item.models import Item
from payment.forms.payment_form import PaymentForm
from payment.models import Payment


def payment_screen(request, id):
    bid = get_object_or_404(Bid, pk=id)
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = bid.bidder
            payment.bid = bid
            payment.save()
            return redirect("review_payment", id=payment.id)
    payment = PaymentForm()
    context = {
        "form": payment,
        "id": id
    }

    return render(request, "payment/single_payment.html", context)


def review_and_process_payment(request, id):
    payment = Payment.objects.get(pk=id)
    if request.method == "POST":
        payment.is_processed = True
        payment.save()
        payment.bid.item.item_listed = False
        payment.bid.item.save()
        messages.success(request, f"Your, payment was successful!")
        return redirect("frontpage")
    context = {
        "payment": payment
    }
    return render(request,"payment/payment_review_page.html", context)
