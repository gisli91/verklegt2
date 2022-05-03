from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
items = [
    {"name": "Köttur til sölu", "price": 1000, "description": "svartur og grimmur"},
    {"name": "Antík vatnabátur", "price": 1200000, "description": "Flýtur"}
]
# Create your views here.
def index(request):
    return render(request, "item/index.html", context={"items": items})