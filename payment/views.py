from django.shortcuts import render, get_object_or_404


# Create your views here.
from bid.models import Bid


def make_payment(request, id):
    bid = get_object_or_404(Bid, pk=id)

    return render("payment/single_payment.html")