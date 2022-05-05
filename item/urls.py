from django.urls import path
from . import views


urlpatterns = [
    # http://localhost:8000/items
    path('', views.index, name="item-index"),
    path('create_item', views.auction_item, name="create_item"),

]
