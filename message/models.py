from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from bid.models import Bid


class Message(models.Model):
    message_content = models.CharField(max_length=255)
    sender = models.ForeignKey(User, related_name="message_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="message_receiver", on_delete=models.CASCADE)
    date_sent = models.DateTimeField(default=datetime.now(), blank=True)
    subject_header = models.CharField(max_length=255)
    is_bid = models.BooleanField(default=False)
    bid_id = models.ForeignKey(Bid, related_name="bid_id", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sender}"
