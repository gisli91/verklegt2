from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from item.models import Item
from user.forms.user_forms import UserSignupForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect, get_object_or_404
from user.forms.profile_form import ProfileForm



# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = ProfileForm().save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, f"Your Profile Has Been Created")
            return redirect("login")
        else:
            messages.error(request, "Invalid password input, please check guidelines.")

    return render(request, "user/register.html", {
        "form": UserSignupForm()
    })

@login_required
def profile(request):
    if request.method == "POST":
        user_update_from = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_from.is_valid() and profile_update_form.is_valid():
            user_update_from.save()
            profile_update_form.save()
            messages.success(request, f"Your profile has been updated")
            return redirect("profile")
    else:
        user_update_from = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": user_update_from,
        "p_form": profile_update_form,
        "user_items": Item.objects.filter(seller=request.user)
    }

    return render(request, "user/profile.html", context)

def some_profile(request,id):
    user = get_object_or_404(User, pk=id)
    if user == request.user:
        return redirect("profile")
    return render(request, "user/some_user.html", {"user": user})