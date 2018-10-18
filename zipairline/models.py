from django.db import models


class ZipAirline(models.Model):
    zipairline_id = models.IntegerField()
    passenger_numb = models.IntegerField()