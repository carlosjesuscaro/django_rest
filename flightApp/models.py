from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.


class Passenger(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    email = models.CharField(max_length=40, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    passport = models.IntegerField


class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirline = models.CharField(max_length=10)
    departureCity = models.CharField(max_length=10)
    arrivalCity = models.CharField(max_length=10)
    dateDeparture = models.DateField()
    timeDeparture = models.TimeField()


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        

