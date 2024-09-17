from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=10)
    password=models.CharField(max_length=30)
    is_active=models.IntegerField(default=1)

class product(models.Model):
    Name=models.CharField(max_length=25)
    Description=models.CharField(max_length=35)
    Price=models.CharField(max_length=25)
    Quantity=models.CharField(max_length=25)
    is_active=models.IntegerField(default=1)

class cart(models.Model):
    userid=models.IntegerField()
    productid=models.IntegerField()
    date=models.DateField()

class order(models.Model):
    userid=models.IntegerField()
    productid=models.IntegerField()
    date=models.DateField()
    address=models.CharField(max_length=25)
    Quantity=models.CharField(max_length=25)
    is_delivered=models.IntegerField(default=0)
    