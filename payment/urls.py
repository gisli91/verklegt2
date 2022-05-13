from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.payment_screen, name="make_payment"),
    path('review_payment/<int:id>/', views.review_and_process_payment, name="review_payment"),

]
