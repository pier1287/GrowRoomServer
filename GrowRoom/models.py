from django.db import models
from django.utils import timezone
from .DHT22 import sensor
import pigpio

pi = pigpio.pi()
dht22 = sensor(pi, 18)
dht22.trigger()
sleepTime = 3

class Measurement (models.Model):
    """Classe che identifica una misurazione generica effettuata mediante un sensore"""

    date_m = models.DateTimeField(default=timezone.now)
    type_m = models.CharField(max_length=128)
    value = models.FloatField()

    class Meta:
        db_table = 'measurement'


class Temperature (Measurement):
    """Classe che identifica le misurazioni di tipo temperatura"""

    @classmethod
    def read(cls):
        dht22.trigger()
        temp_value = repr(dht22.temperature())
        date = timezone.now
        temp = cls(value=temp_value,date_m=date,type_m='t')
        return temp


class Humidity (Measurement):
    """Classe che identifica le misurazioni di tipo umidita"""

    @classmethod
    def read(cls):
        dht22.trigger()
        humidity_value = repr(dht22.humidity())
        date = timezone.now
        hygro = cls(value=humidity_value, date_m=date, type_m='h')
        return hygro

