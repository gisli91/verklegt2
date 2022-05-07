# Generated by Django 4.0.4 on 2022-05-07 04:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('receiver', models.CharField(max_length=50)),
                ('date_sent', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 7, 4, 31, 16, 375221))),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
