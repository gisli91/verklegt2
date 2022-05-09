from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from user.models import User
from .forms.message_form import MessageForm
from .models import Message
import time
# Create your views here.
from django.http import HttpResponse


# Create your views here.
def inbox(request):
    context = {"messages": Message.objects.filter(receiver=request.user)}
    return render(request, "message/index.html", context)


def reply(request):
    return render(request, "message/index.html")


def send(request):

    if request.method == "POST":
        data = request.POST.copy()

        form = MessageForm(data)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, "Your message has been sent")

            return redirect("message-inbox")
    else:
        message = MessageForm()

    context = {
        "form": message,

    }
    return render(request, "message/send_message.html", context)