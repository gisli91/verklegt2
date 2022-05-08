from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Message(models.Model):
    message_content = models.CharField(max_length=255)
    sender = models.ForeignKey(User, related_name="message_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="message_receiver", on_delete=models.CASCADE)
    date_sent = models.DateTimeField(default=datetime.now(), blank=True)
    subject_header = models.CharField(max_length=255)
