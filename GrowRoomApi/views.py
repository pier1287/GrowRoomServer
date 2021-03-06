from rest_framework import viewsets
from rest_framework.decorators import detail_route,list_route
from rest_framework.response import Response
from django.contrib.auth.models import User
from . import serializers
from GrowRoom.models import Measurement,Temperature,Humidity


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = serializers.TemperatureSerializer

    @list_route(methods=['get'])
    def latest(self, request,pk=None):
        latest_temperature = Temperature.read()
        serializer = self.get_serializer(latest_temperature)
        return Response(serializer.data)


class HumidityViewSet(viewsets.ModelViewSet):
    queryset = Humidity.objects.all()
    serializer_class = serializers.HumiditySerializer

    @list_route(methods=['get'])
    def latest(self, request,pk=None):
        latest_humidity = Humidity.read()
        serializer = self.get_serializer(latest_humidity)
        return Response(serializer.data)
