# Generated by Django 4.0.4 on 2022-05-13 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0034_alter_bid_bid_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 13, 16, 33, 14, 11718)),
        ),
    ]
