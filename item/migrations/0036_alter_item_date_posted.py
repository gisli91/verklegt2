# Generated by Django 4.0.4 on 2022-05-13 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0035_alter_item_category_alter_item_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 13, 16, 33, 14, 9718)),
        ),
    ]
