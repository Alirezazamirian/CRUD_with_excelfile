from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Passenger(models.Model):
    PCLASS_CHOICES = [
        (1, 'First class'),
        (2, 'Second class'),
        (3, 'Third class')
    ]

    SEX_CHOICES = [
        ('male', 'male'),
        ('female', 'female')
    ]

    EMBARK = [
        ('S', 'southhampton'),
        ('C', 'sherburg'),
        ('Q', 'queentown')
    ]

    survived = models.BooleanField(verbose_name='غرق شده')
    pclass = models.PositiveIntegerField(verbose_name='کلاس بلیت', choices=PCLASS_CHOICES)
    name = models.CharField(max_length=100, verbose_name='نام')
    sex = models.CharField(max_length=10, verbose_name='جنسیت', choices=SEX_CHOICES)
    age = models.FloatField(verbose_name='سن', validators=[MaxValueValidator(120), MinValueValidator(1)], blank=True,
                            null=True)
    sibsp = models.IntegerField(verbose_name='تعداد همسر و خواهر و برادر ',
                                validators=[MaxValueValidator(10), MinValueValidator(0)])
    parch = models.IntegerField(verbose_name='تعداد فرزندان و پدر و مادر ',
                                validators=[MaxValueValidator(10), MinValueValidator(0)])
    ticket = models.CharField(max_length=20, verbose_name='کد بلیت')
    fare = models.FloatField(verbose_name='کرایه(پوند)')
    cabin = models.CharField(verbose_name='شماره کابین', max_length=20, null=True, blank=True)
    embarked = models.CharField(verbose_name='بندر سوار شده', choices=EMBARK)

    def __str__(self):
        return self.name + " - " + str(self.age)
