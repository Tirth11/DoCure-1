from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class User(AbstractUser):
    age=models.IntegerField(null=False, default=0)
    gender=models.CharField(choices=[('Male','Male'),('Female','Female')],max_length=15)
    height=models.IntegerField(null=False, default=0)
    weight=models.IntegerField(null=False, default=0)

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()

class Cbc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rbc = models.FloatField()
    wbc = models.FloatField()
    pc = models.FloatField()
    

