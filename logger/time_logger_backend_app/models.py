from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class MilPerson(models.Model):
    rank = models.CharField(max_length=30, blank=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    # func_on_board = models.ForeignKey(to=FunctionOnBoard,on_delete=models.CASCADE,related_name='users')
    user = models.ForeignKey(to=User,on_delete=models.CASCADE, blank=True, related_name='credentials')
#
#
# class FunctionOnBoard(models.Model):
#     CHOICES = (
#         ("pilot", "PILOT"),
#         ("technician", "TECHNIK"),
#         ("gunner", "STRZELEC"),
#         ("medic", "RATOWNIK"),
#         ("other", "INNY"),
#     )
#     name = models.TextField(max_length=255, choices=CHOICES)
#     user = models.ManyToManyField(MilPerson, related_name='mil_person')





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
