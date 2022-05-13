from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from bid.models import Bid
from payment.models import Payment
from .models import Message
from django.contrib.auth.models import User


@receiver(post_save, sender=Bid)
def receive_bid(sender, instance, created, *args, **kwargs):
    if created:
        content = f"You have received a new ${instance.bid_amount} bid for {instance.item.name} from user {instance.bidder}"
        header = f"New bid for {instance.item.name}"
        sender = User.objects.filter(username="Notifications").first()

        Message.objects.create(message_content=content,
                               subject_header=header,
                               sender=sender,
                               receiver=instance.item.seller,
                               is_bid=True,
                               bid_id=instance),



