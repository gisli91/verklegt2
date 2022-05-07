from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Message(models.Model):
    content = models.CharField(max_length=255)
    sender = models.ForeignKey(User, related_name="message_sender", on_delete=models.CASCADE)
    receiver = models.CharField(max_length=50)
    date_sent = models.DateTimeField(default=datetime.now(), blank=True)
