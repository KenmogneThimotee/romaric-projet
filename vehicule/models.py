from distutils.command.upload import upload
from operator import mod
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vehicule(models.Model):

    price = models.FloatField()
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=49)
    rent_price = models.FloatField()
    ondometer = models.FloatField()
    transmition = models.CharField(choices=[('manual', 'manual'), ('auto', 'auto')], max_length=30)
    seats = models.IntegerField()
    fuel = models.CharField(choices=[('petrol', 'petrol'), ('gazoil', 'gazoil')], max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to="media")
    luggage = models.IntegerField()
    user = models.ManyToManyField(User, through='Location') 
    pass 

class Location(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    
    pickup_location = models.CharField(max_length=25)
    dropoff_location = models.CharField(max_length=25)
    pickup_date = models.DateField()
    dropoff_date = models.DateField()
    pickup_time = models.TimeField()

    dropoff = models.BooleanField(default=False)
     

class Contact(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()