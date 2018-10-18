from math import log
from .settings import PER_PASSENGER_CONSUMPTION, PER_PLANE_CONSUMPTION, FIELD_TANK


class ZipAirplaneUtils:

    @staticmethod
    def field_tank(zipairline_id):
        return zipairline_id * FIELD_TANK

    @staticmethod
    def fly_time(zipairline_id, passenger_numb):
        return ZipAirplaneUtils.field_tank(zipairline_id) / ZipAirplaneUtils.total_consumption_per_minute(zipairline_id, passenger_numb)

    @staticmethod
    def total_consumption_per_minute(zipairline_id, passenger_numb):
        passengers_consumption_per_minute = passenger_numb * PER_PASSENGER_CONSUMPTION
        airplane_consumption_per_minue = log(zipairline_id ** PER_PLANE_CONSUMPTION, 10)
        return passengers_consumption_per_minute + airplane_consumption_per_minue
