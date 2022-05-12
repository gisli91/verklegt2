from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from payment.forms.payment_form import PaymentForm
from user.models import User
from .forms.message_form import MessageForm
from .forms.reply_message_form import ReplyMessageForm
from .models import Message
import time
# Create your views here.
from django.http import HttpResponse


# Create your views here.
def inbox(request):
    context = {"messages": Message.objects.filter(receiver=request.user).exclude(sender=request.user)}
    return render(request, "message/index.html", context)


def reply(request, id):
    receiver = get_object_or_404(User, pk=id)
    if receiver.username == "Notifications":
        return redirect("message-inbox")
    if request.method == "POST":
        form = ReplyMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = receiver
            message.save()
            messages.success(request, "Your message has been sent")

            return redirect("message-inbox")
    else:
        message = ReplyMessageForm()

    context = {
        "form": message,
    }
    return render(request, "message/send_message.html", context)


def get_message_by_id(request, id):
    message = get_object_or_404(Message, pk=id)
    if message.is_bid_accepted:
        form = PaymentForm()
        return render(request, "message/message_details.html", {
            "message": get_object_or_404(Message, pk=id),
            "form": form
        })

    return render(request, "message/message_details.html", {
        "message": get_object_or_404(Message, pk=id)
    })


def delete(request, id):
    message = get_object_or_404(Message, pk=id)
    message.delete()
    return redirect("message-inbox")

def send(request):
    if request.method == "POST":

        form = MessageForm(request.POST)
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
