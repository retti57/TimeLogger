import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class MilPerson(models.Model):
    class Meta:
        verbose_name = 'Personel'
        verbose_name_plural = 'Personel latający'

    CHOICES = (
        ("pilot", "PILOT"),
        ("technician", "TECHNIK"),
        ("gunner", "STRZELEC"),
        ("medic", "RATOWNIK"),
        ("other", "INNY"),
    )

    rank = models.CharField(max_length=30, blank=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True, related_name='credentials')
    function_on_board = models.TextField(max_length=255, choices=CHOICES, blank=True, null=True)

    def __str__(self):
        return f'{self.rank} {self.last_name.upper()} {self.first_name}'

class Aircraft(models.Model):
    class Meta:
        verbose_name = 'Śmigłowiec'
        verbose_name_plural = 'Śmigłowce'

    AC_TYPES = (
        ("W-3", "W-3"),
        # ("Mi-2", "Mi-2"),
    )
    W3_NUMBERS = (
        ('0901', '0901'),
        ('0819', '0819'),
        ('0820', '0820'),
        ('0618', '0618'),
        ('0615', '0615'),
        ('0609', '0609'),
    )
    aircraft_type = models.CharField(max_length=255, default="W-3", choices=AC_TYPES, blank=False, null=True)
    aircraft_number = models.CharField(max_length=30, blank=False, choices=W3_NUMBERS)

    def __str__(self):
        return f'{self.aircraft_type} {self.aircraft_number}'


class Log(models.Model):
    class Meta:
        verbose_name_plural = 'Logi'

    aircraft = models.ForeignKey(to=Aircraft, on_delete=models.CASCADE, related_name='aircraft', verbose_name='Śmigłowiec')
    exercise = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ćwiczenie')
    # czas
    date_of_flight = models.DateField(auto_now=True)
    start_up = models.DateTimeField(default= datetime.datetime.now(),verbose_name='Uruchomienie[UTC]')
    take_off = models.DateTimeField(default= datetime.datetime.now() ,verbose_name='Start[UTC]')
    land = models.DateTimeField(default= datetime.datetime.now(),verbose_name='Lądowanie[UTC]')
    shut_down = models.DateTimeField(default= datetime.datetime.now() ,verbose_name='Wyłączenie[UTC]')

    # załoga
    crew = models.ManyToManyField(to=MilPerson, verbose_name='Załoga')

    def __str__(self):
        return f"{self.aircraft} {self.date_of_flight}"

