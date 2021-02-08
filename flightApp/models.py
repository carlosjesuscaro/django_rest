from django.db import models

# Create your models here.


class Passenger(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    passport = models.IntegerField(max_length=10)
    phone = models.CharField(max_length=10)


class Flight(models.Model):
    flightNumber = models.IntegerField(max_length=5)
    operatingAirline = models.CharField(max_length=10)
    departureCity = models.CharField(max_length=10)
    arrivalCity = models.CharField(max_length=10)
    dateDeparture = models.DateField()
    timeDeparture = models.TimeField()


class Reservation(models.Model):
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE())
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE())