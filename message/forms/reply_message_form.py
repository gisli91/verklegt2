from django import forms
from django.core.exceptions import ValidationError


from message.models import Message


class ReplyMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["subject_header", "message_content"]




