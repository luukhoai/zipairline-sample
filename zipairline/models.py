from math import log
from django.db import models
from .settings import PER_PASSENGER_CONSUMPTION, PER_PLANE_CONSUMPTION, FIELD_TANK


class ZipAirline(models.Model):
    airline_name = models.CharField(max_length=100)


class ZipAirplane(models.Model):
    airplane_id = models.IntegerField()
    passenger_numb = models.IntegerField()
    airline = models.ForeignKey(ZipAirline, related_name='airplanes', on_delete=models.CASCADE)

    @property
    def field_tank(self):
        return self.airplane_id * FIELD_TANK

    @property
    def fly_time(self):
        return self.field_tank / self.total_consumption_per_minute

    @property
    def total_consumption_per_minute(self):
        return self.passengers_consumption_per_minute() + self.airplane_consumption_per_minue()

    def passengers_consumption_per_minute(self):
        return self.passenger_numb * PER_PASSENGER_CONSUMPTION

    def airplane_consumption_per_minue(self):
        return log(self.airplane_id ** PER_PLANE_CONSUMPTION, 10)

