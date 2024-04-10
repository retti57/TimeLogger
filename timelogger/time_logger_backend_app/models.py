from django.db import models

# Create your models here.
class UserModel(models.Model):
    class FuncOnBoard(models.TextChoices):
        PILOT = "P"
        TECHNIK = "T"
        STRZELEC = "S"
        RATOWNIK = "R"
        INNY = "O"

    func_on_board = models.TextField(choices=FuncOnBoard.choices)
    rank = models.CharField(max_length=10, blank=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
