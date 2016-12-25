from django.db import models
from django.utils import timezone
from .DHT22 import sensor
import pigpio

#Inizializzazione sensore Temperatura - Umidita
pi = pigpio.pi()
dht22 = sensor(pi, 18)
dht22.trigger()
sleepTime = 3


class Temperature (models.Model):
    """Classe che identifica le misurazioni di tipo temperatura"""

    date_m = models.DateTimeField(default=timezone.now)
    value = models.FloatField()

    @classmethod
    def read(cls):
        dht22.trigger()
        temp_value = repr(dht22.temperature())
        date = timezone.now()
        temp = cls(value=temp_value,date_m=date)
        return temp

    class Meta:
        db_table = 'temperature'


class Humidity (models.Model):
    """Classe che identifica le misurazioni di tipo umidita"""

    date_m = models.DateTimeField(default=timezone.now)
    value = models.FloatField()

    @classmethod
    def read(cls):
        dht22.trigger()
        humidity_value = repr(dht22.humidity())
        date = timezone.now()
        hygro = cls(value=humidity_value, date_m=date)
        return hygro

    class Meta:
        db_table = 'humidity'


class Measurement (models.Model):
    """Classe che identifica una misurazione generica effettuata mediante un sensore"""

    date_m = models.DateTimeField(default=timezone.now)
    type_m = models.CharField(max_length=1)
    value = models.FloatField()

    class Meta:
        db_table = 'measurement'
