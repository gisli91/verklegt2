from django.forms import ModelForm, widgets

from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["id", "user"]
        widgets = {
            "bio": widgets.Textarea(attrs={ "class": "form-control"}),
        }