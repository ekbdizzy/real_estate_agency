# Generated by Django 2.2.20 on 2021-05-03 15:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
