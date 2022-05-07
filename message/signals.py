from django.db.models.signals import post_save
from django.dispatch import receiver
from bid.models import Bid
from .models import Message




@receiver(post_save, sender=Bid)
def receive_bid(sender, instance, created, **kwargs):
    if created:
        Message.objects.create(content="blablabla", sender=instance.bidder, receiver=instance.item.seller)
