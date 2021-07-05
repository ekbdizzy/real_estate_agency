# Generated by Django 2.2.20 on 2021-07-05 14:46
import phonenumbers
from django.db import migrations


def parse_phone(number, country="RU"):
    parsed_number = phonenumbers.parse(number, country)
    country_code, number = parsed_number.country_code, parsed_number.national_number
    return f"+{country_code}{number}"


def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = parse_phone(flat.owner_phone_number)
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0011_auto_20210705_1742'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone)
    ]
