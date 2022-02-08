from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=15)
    password=models.CharField(max_length=10)
    # password2=models.CharField(max_length=10)