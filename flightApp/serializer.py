from rest_framework import serializers
from .models import Flight, Passenger, Reservation
import re # re -> regular expressions


def isFlightNumberValid(flightNumber):
    print('isFlightNumberValid')


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators=[isFlightNumberValid]

    def validate_flightNumber(self, flightNumber):
        print('validate flight_number')
        if (re.match("^[a-zA-Z0-9]*$", flightNumber)==None):  # validating that the flight number is alpha numeric
            raise serializers.ValidationError("Invalid flight number")
        return flightNumber


    def validate(self, data):
        print('validate')
        print(data)
        return data


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
