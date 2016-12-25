from rest_framework import serializers
from django.contrib.auth.models import User
from GrowRoom.models import Measurement,Temperature, Humidity


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','id', 'username', 'email', 'is_staff')


class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurement
        fields = ('id', 'date_m', 'value')


class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = ('id', 'date_m', 'value')


class HumiditySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Humidity
        fields = ('id', 'date_m', 'value')