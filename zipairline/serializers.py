from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import ZipAirline
from .utils import ZipAirplaneUtils


class ZipAirlineSerializer(ModelSerializer):

    class Meta:
        model = ZipAirline
        fields = ('zipairline_id', 'passenger_numb', 'total_consumption_per_minute', 'fly_time')

    def validate_zipairline_id(self, value):
        if value < 0:
            raise serializers.ValidationError('zipairline_id should be positive integer value.', code='input')
        return value

    def validate_passenger_numb(self, value):
        if value < 0:
            raise serializers.ValidationError('passenger_numb shoud be positive integer value.')
        return value

    def validate(self, order_dict):
        zipairline_id = order_dict['zipairline_id']
        passenger_numb = order_dict['passenger_numb']
        fly_time = ZipAirplaneUtils.fly_time(zipairline_id, passenger_numb)
        if fly_time < 1:
            raise serializers.ValidationError('fly_time should be larger than 1.')
        return order_dict