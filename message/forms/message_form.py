from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import Textarea

from message.models import Message


class MessageForm(forms.ModelForm):
    class Meta:

        model = Message
        fields = ["subject_header", "message_content", "receiver"]
        labels = {
            "subject_header": _("Subject"),
            "message_content": _("Your message"),
            "receiver": _("Recipient")
        }
        widgets = {
            "message_content": Textarea(attrs={'rows': 12})
        }






