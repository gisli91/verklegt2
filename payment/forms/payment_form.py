from django import forms
from payment.models import Payment
from django.utils.translation import gettext_lazy as _


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["name", "address", "zip_code","country" ,"card_nr", "cvc_nr", "exp_date"]
        labels = {
            "name": _("Cardholder's full name"),
            "address": _("Address (Street, City)"),
            "zip_code": _("Zip Code"),
            "country": _("Country"),
            "card_nr": _("Card number"),
            "cvc_nr": _("Cvc number"),
            "exp_date": _("Expiration date")
        }






