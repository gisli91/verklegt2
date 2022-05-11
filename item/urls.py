from django.urls import path
from . import views


urlpatterns = [
    # http://localhost:8000/items
    path('', views.index, name="item-index"),
    path('create_item', views.auction_item, name="create_item"),
    path('<int:id>', views.get_item_by_id, name="item_details"),
    path('delete_item/<int:id>', views.delete_item, name="delete_item"),
    path('update_item/<int:id>', views.update_item, name="update_item"),

]
