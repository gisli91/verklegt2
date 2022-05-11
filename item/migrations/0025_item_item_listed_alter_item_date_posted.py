# Generated by Django 4.0.4 on 2022-05-11 01:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0024_alter_item_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_listed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 11, 1, 1, 6, 719829)),
        ),
    ]
