from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from item.forms.item_form import ItemCreateForm
from item.models import Item
from .models import Message


# Create your views here.
from django.http import HttpResponse

# Create your views here.
def inbox(request):
    context = {"messages": Message.objects.filter(receiver=request.user)}
    return render(request, "message/index.html", context)



