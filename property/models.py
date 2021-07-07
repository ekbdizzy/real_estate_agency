from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200, db_index=True)
    phone_number = models.CharField('Номер владельца', max_length=20, db_index=True)
    pure_phone = PhoneNumberField('Нормализованный номер телефона', blank=True, null=True, db_index=True)
    flats = models.ManyToManyField(to='Flat',
                                   blank=True,
                                   related_name='flats',
                                   verbose_name='Квартиры в собственности',
                                   )

    def __str__(self):
        return self.name


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    new_building = models.NullBooleanField("Новостройка", db_index=True)
    liked_by = models.ManyToManyField(User,
                                      blank=True,
                                      related_name='likes',
                                      verbose_name='Кто лайкнул')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Кто жалуется',
                               related_name="complaints")
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE,
                             verbose_name='Квартира, на которую пожаловались',
                             related_name='complaints')
    text = models.TextField(blank=True, null=True, verbose_name='Текст жалобы')

    def __str__(self):
        return f"{self.pk}: {self.author}, {self.flat.town}, {self.flat.address}"
