from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.make_bid, name="make_bid"),
    path('accept/<int:id>/', views.accept_bid, name="accept_bid")
]
