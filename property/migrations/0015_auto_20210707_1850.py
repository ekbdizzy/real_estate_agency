# Generated by Django 2.2.20 on 2021-07-07 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20210706_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_phone_number',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
    ]
