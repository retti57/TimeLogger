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


# class Pilot(models.Model):
#     class Meta:
#         verbose_name_plural = "Piloci"
#     id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     user = models.ManyToManyField(related_name='func_on_board', to=MilPerson)

class Aircraft(models.Model):
    class Meta:
        # verbose_name = 'Funkcja'
        verbose_name_plural = 'Śmigłowce'

    AC_TYPES = (
        ("w3", "W-3"),
        # ("mi2", "Mi-2"),
    )
    W3_NUMBERS = (
        ('0901', '0901'),
        ('0819', '0819'),
        ('0820', '0820'),
        ('0615', '0615'),
        ('0609', '0609'),
    )
    aircraft_type = models.TextField(max_length=255, default="w3", choices=AC_TYPES, blank=True, null=True)
    aircraft_number = models.CharField(max_length=30, blank=False)




# class MilPerson(User):
#
# class Log(models.Model):
# załoga
## każdy z członków załogi do wybrania z oddzielnej tabeli na podstawie klucza zewn

# śmigłowiec
## śmigłowiec na podstawie tabeli

# czasy
# uruchomienie
# start
# lądowanie
# wyłączenie
