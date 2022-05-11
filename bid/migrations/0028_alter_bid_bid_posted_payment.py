# Generated by Django 4.0.4 on 2022-05-11 03:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0027_alter_bid_bid_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 11, 3, 37, 0, 830973)),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('card_nr', models.IntegerField(max_length=30)),
                ('card_cvc', models.IntegerField(max_length=3)),
                ('card_expiration', models.CharField(max_length=5)),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bid.bid')),
            ],
        ),
    ]