# Generated by Django 4.0.4 on 2022-05-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_alter_payment_card_nr_alter_payment_cvc_nr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_processed',
            field=models.BooleanField(default=False),
        ),
    ]