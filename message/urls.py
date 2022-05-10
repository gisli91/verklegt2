from django.urls import path
from . import views


urlpatterns = [
    # http://localhost:8000/messages
    path('', views.inbox, name="message-inbox"),
    #path('new', views.new_message, name="new_message"),
    path('new', views.send, name="send_message"),
    path('reply/<int:id>/', views.reply, name="reply_message"),
    path('<int:id>/', views.delete, name="delete_message"),

]
