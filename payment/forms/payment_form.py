from django import forms
from payment.models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["user", "bid", "name", "card_nr", "cvc_nr", "exp_date"]







