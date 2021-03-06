# Generated by Django 4.0.4 on 2022-05-12 04:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bid', '0030_alter_bid_bid_posted'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('card_nr', models.IntegerField(blank=True)),
                ('cvc_nr', models.IntegerField(blank=True)),
                ('exp_date', models.IntegerField(blank=True)),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bid.bid')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
