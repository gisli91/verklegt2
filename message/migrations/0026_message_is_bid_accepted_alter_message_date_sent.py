# Generated by Django 4.0.4 on 2022-05-12 04:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0025_alter_message_date_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_bid_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='date_sent',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 12, 4, 35, 9, 529217)),
        ),
    ]
