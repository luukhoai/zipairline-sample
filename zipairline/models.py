from math import log
from django.db import models
from .settings import PER_PASSENGER_CONSUMPTION, PER_PLANE_CONSUMPTION, FIELD_TANK


class ZipAirplane(models.Model):
    airplane_id = models.IntegerField()
    passenger_numb = models.IntegerField()

    @property
    def field_tank(self):
        return self.airplane_id * FIELD_TANK

    @property
    def fly_time(self):
        return self.field_tank / self.total_consumption_per_minute

    @property
    def total_consumption_per_minute(self):
        return self.passengers_consumption_per_minute + self.airplane_consumption_per_minue

    @property
    def passengers_consumption_per_minute(self):
        return self.passenger_numb * PER_PASSENGER_CONSUMPTION

    @property
    def airplane_consumption_per_minue(self):
        return log(self.airplane_id ** PER_PLANE_CONSUMPTION, 10)
