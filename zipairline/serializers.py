from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import ZipAirplane, ZipAirline


class ZipAirplaneSerializer(ModelSerializer):

    class Meta:
        model = ZipAirplane
        fields = ('airplane_id', 'passenger_numb', 'airline','total_consumption_per_minute', 'fly_time')

    def validate_airplane_id(self, value):
        if value < 0:
            raise serializers.ValidationError('airplane_id should be positive integer value.', code='input')
        return value

    def validate_passenger_numb(self, value):
        if value < 0:
            raise serializers.ValidationError('passenger_numb shoud be positive integer value.')
        return value

    def validate(self, order_dict):
        airplane_id = order_dict['airplane_id']
        passenger_numb = order_dict['passenger_numb']
        airline = ZipAirplane(airplane_id=airplane_id, passenger_numb=passenger_numb)
        if airline.fly_time < 1:
            raise serializers.ValidationError('fly_time should be larger than 1.')
        return order_dict


class ZipAirlinesSerializer(ModelSerializer):
    airplanes = ZipAirplaneSerializer(many=True)

    class Meta:
        model = ZipAirline
        fields = ('airplanes', 'airline_name', 'total_consumption', 'total_fly_time')

    def create(self, validated_data):
        airline_name = validated_data.pop('airline_name')
        airplanes = validated_data.pop('airplanes')

        airline = ZipAirline.objects.get(airline_name=airline_name)
        for airplane_data in airplanes:
            ZipAirplane.objects.create(**airplane_data)
        return airline

