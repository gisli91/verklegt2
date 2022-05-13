from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.payment_screen, name="make_payment"),

]
