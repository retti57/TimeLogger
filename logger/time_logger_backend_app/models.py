from django.contrib.auth.models import User
from django.db import models


class Notes(models.Model):
    date_of_note = models.DateField(auto_now=True)
    note = models.CharField(max_length=1255, default='-', blank=True, null=True, verbose_name='Notatka')

    class Meta:
        verbose_name = 'Notatka'
        verbose_name_plural = 'Notatki'

    def __str__(self):
        return f'{self.date_of_note} {self.note[:50]}(...)'


class MilPerson(models.Model):
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

    class Meta:
        verbose_name = 'Personel'
        verbose_name_plural = 'Personel latający'

    def __str__(self):
        return f'{self.rank} {self.last_name.upper()} {self.first_name}'


class Aircraft(models.Model):
    AC_TYPES = (
        ("W-3", "W-3"),
    )

    W3_NUMBERS = (
        ('0901', '0901'),
        ('0819', '0819'),
        ('0820', '0820'),
        ('0618', '0618'),
        ('0615', '0615'),
        ('0609', '0609'),
        ('0609', '0601'),
    )
    aircraft_type = models.CharField(max_length=255, default="W-3", choices=AC_TYPES, blank=False)
    aircraft_number = models.CharField(max_length=30, blank=False, choices=W3_NUMBERS)
    notes = models.ForeignKey(to=Notes, on_delete=models.CASCADE, null=True, blank=True, related_name='aircraft_notes',
                              verbose_name='Uwagi')

    class Meta:
        verbose_name = 'Śmigłowiec'
        verbose_name_plural = 'Śmigłowce'

    def __str__(self):
        return f'{self.aircraft_type} {self.aircraft_number}'


class Log(models.Model):
    aircraft = models.ForeignKey(to=Aircraft, on_delete=models.CASCADE, related_name='aircraft',
                                 verbose_name='Śmigłowiec')
    exercise = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ćwiczenie')
    # czas

    date_of_flight = models.DateField(auto_now=False, verbose_name='Data lotu')
    start_up = models.DateTimeField(
        verbose_name='Uruchomienie[UTC]',
        null=False
    )
    take_off = models.DateTimeField(
        verbose_name='Start[UTC]',
        null=False
    )
    land = models.DateTimeField(
        verbose_name='Lądowanie[UTC]',
        null=False
    )
    shut_down = models.DateTimeField(
        verbose_name='Wyłączenie[UTC]',
        null=False
    )

    # załoga
    crew = models.ManyToManyField(to=MilPerson, verbose_name='Załoga')

    ## rozkaz / PTL
    # order_to_fly = models.ForeignKey(to=Order,on_delete=models.DO_NOTHING, related_name='Order')

    class Meta:
        verbose_name_plural = 'Logi'

    def __str__(self):
        crew_list = [p.last_name for p in self.crew.all()]
        crew = ' '.join(crew_list)

        return f"{self.aircraft} - {self.start_up.date()} {self.exercise} || {crew}"


class OrderForFlight(models.Model):
    number = models.PositiveIntegerField(verbose_name='Numer rozkazu', unique=True)
    log = models.ForeignKey(to=Log, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Rozkazy do lotu'
