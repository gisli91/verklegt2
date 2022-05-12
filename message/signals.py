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


@receiver(pre_save, sender=Payment)
def bid_accepted(sender, instance, *args, **kwargs):
    content = f"Your bid for ${instance.bid.bid_amount} for item {instance.bid.item} from user {instance.bid.bidder}" \
              f" Please provide your payment information"
    header = f"Your bid for  {instance.bid.item.name} has been accepted!"
    sender = User.objects.filter(username="Notifications").first()

    Message.objects.create(message_content=content,
                           subject_header=header,
                           sender=sender,
                           receiver=instance.bid.bidder,
                           is_bid=True,
                           bid_id=instance.bid,
                           is_bid_accepted=True),
