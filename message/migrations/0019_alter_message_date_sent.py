# Generated by Django 4.0.4 on 2022-05-11 01:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0018_alter_message_date_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_sent',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 11, 1, 1, 6, 720828)),
        ),
    ]
