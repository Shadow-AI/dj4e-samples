from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator


# Create your models here.
class Make(models.Model):
    name = models.CharField(max_length=200, help_text='Enter Make of vehicle',
                            validators=[MinLengthValidator(2, 'make must be longer than 1 characters')])

    def __str__(self):
        return self.name


class Auto(models.Model):
    nickname = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, 'length should be more than 1 character')]
    )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=200, blank=True)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname

