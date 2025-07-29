from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    groups = models.ManyToManyField(
            'auth.Group',
            related_name='customuser_set',  # related_name bilan to'qnashuv oldini olish
            blank=True
        )
    user_permissions = models.ManyToManyField(
            'auth.Permission',
            related_name='customuser_set_permissions',  # related_name bilan to'qnashuv oldini olish
            blank=True
        )
    def __str__(self):
        return self.username


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Group(models.Model):
    DAYS = (
        ('Odd', 'Odd'),
        ('Even', 'Even'),
        ('Weekend', 'Weekend'),
    )
    name = models.CharField(max_length=100, unique=True)
    day = models.CharField(max_length=10, choices=DAYS)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Teacher(CustomUser):
    GRADING = (
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior'),
    )
    rating = models.FloatField(default=0)
    grading = models.CharField(max_length=10, choices=GRADING, default='Junior')
    salary = models.FloatField(default=0)

class Student(CustomUser):
    RATINGS = (
        ('Iron', 'Iron'),
        ('Bronze', 'Bronze'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
        ('Marsianin', 'Marsianin'),
    )
    coins = models.IntegerField(default=0)
    power = models.IntegerField(default=0)
    coin_rating = models.IntegerField(default=0)
    rating = models.CharField(max_length=10, choices=RATINGS, default='Iron')
    typing_rating = models.IntegerField(default=0)
    strike = models.IntegerField(default=0)
    group = models.ForeignKey('Group', on_delete=models.DO_NOTHING)
    payment = models.IntegerField()
    payment_status = models.BooleanField(default=False)