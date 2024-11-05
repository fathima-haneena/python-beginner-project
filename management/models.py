from django.db import models

# Create your models here.

class form(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    age=models.IntegerField()
    address=models.TextField()
    username=models.CharField(max_length=20,default='null')
class form1(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    age=models.IntegerField()
    address=models.TextField()
    username=models.CharField(max_length=20,default='null')
class form2(models.Model):
    name=models.CharField(max_length=20)
    address=models.TextField()
    age=models.IntegerField()

