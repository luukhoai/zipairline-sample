from django.db import models
from .utils import ZipAirplaneUtils


class ZipAirline(models.Model):
    zipairline_id = models.IntegerField()
    passenger_numb = models.IntegerField()

    @property
    def field_tank(self):
        return ZipAirplaneUtils.field_tank(self.zipairline_id)

    @property
    def fly_time(self):
        return ZipAirplaneUtils.fly_time(self.zipairline_id, self.passenger_numb)

    @property
    def total_consumption_per_minute(self):
        return ZipAirplaneUtils.total_consumption_per_minute(self.zipairline_id, self.passenger_numb)