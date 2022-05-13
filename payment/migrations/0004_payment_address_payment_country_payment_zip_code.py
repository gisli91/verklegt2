# Generated by Django 4.0.4 on 2022-05-13 16:33

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_payment_is_processed'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='payment',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]