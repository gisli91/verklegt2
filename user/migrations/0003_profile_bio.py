# Generated by Django 4.0.4 on 2022-05-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
