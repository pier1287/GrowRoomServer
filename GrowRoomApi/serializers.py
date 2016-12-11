from rest_framework import serializers
from django.contrib.auth.models import User
from GrowRoom.models import Measurement


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','id', 'username', 'email', 'is_staff')


class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurement
        fields = ('id', 'date_m', 'value')