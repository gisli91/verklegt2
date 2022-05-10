from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset

from message.models import Message


class MessageForm(forms.ModelForm):
    class Meta:

        model = Message
        fields = ["subject_header", "message_content", "receiver"]






