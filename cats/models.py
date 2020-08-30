from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(2, 'Length should be more than 1')])

    def __str__(self):
        return self.name


class Cat(models.Model):
    nickname = models.CharField(max_length=200, validators=[MinLengthValidator(2, 'should be more than 1')])
    weight = models.PositiveIntegerField()
    food = models.CharField(max_length=300)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
