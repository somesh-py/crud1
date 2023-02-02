from django.db import models

# Create your models here.
class data(models.Model):
    name=models.CharField(max_length=200)
    mothername=models.CharField(max_length=200)
    fathername=models.CharField(max_length=200)
    contact=models.IntegerField(max_length=20)
    dob=models.DateField()
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)