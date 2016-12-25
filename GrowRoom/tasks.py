from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Temperature,Humidity


@shared_task
def temperature_log():
    print('Reading..')
    temp = Temperature.read()
    print('Temperature:'+temp.value+'Saving..')
    temp.save()
    print('Saved.')


@shared_task
def humidity_log():
    humidity = Humidity.read()
    humidity.save()