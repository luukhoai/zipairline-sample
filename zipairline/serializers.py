from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import ZipAirplane, ZipAirline


class ZipAirplaneSerializer(ModelSerializer):

    class Meta:
        model = ZipAirplane
        fields = ('airplane_id', 'passenger_numb', 'airline')

    def validate_airplane_id(self, value):
        """
        Validate airplane_id, should be positive integer
        :param value:
        :return: value
        """
        if value < 0:
            raise serializers.ValidationError('airplane_id should be positive integer value.', code='input')
        return value

    def validate_passenger_numb(self, value):
        """
        Validate passenger_numb, should be positive integer
        :param value:
        :return:
        """
        if value < 0:
            raise serializers.ValidationError('passenger_numb shoud be positive integer value.')
        return value

    def validate(self, order_dict):
        """
        Validate fly_time, should be larger than 1 minute
        :param order_dict:
        :return: order_dict
        """
        airplane_id = order_dict['airplane_id']
        passenger_numb = order_dict['passenger_numb']
        airline = ZipAirplane(airplane_id=airplane_id, passenger_numb=passenger_numb)
        if airline.fly_time < 1:
            raise serializers.ValidationError('fly_time should be larger than 1.')
        return order_dict


class ZipAirplaneCreateSerializer(ZipAirplaneSerializer):
    class Meta:
        model = ZipAirplane
        fields = ('airplane_id', 'passenger_numb')


class ZipAirlinesSerializer(ModelSerializer):
    airplanes = ZipAirplaneCreateSerializer(many=True)

    class Meta:
        model = ZipAirline
        fields = ('airline_name', 'airplanes')

    def create(self, validated_data):
        """
        Create airplane
        :param validated_data: eg: {'airline_name': 'TestAirline', 'airplanes': [...]}
        :return: airline
        """
        airline_name = validated_data.pop('airline_name')
        airplanes = validated_data.pop('airplanes')

        airline = ZipAirline.objects.get(airline_name=airline_name)
        for airplane_data in airplanes:
            ZipAirplane.objects.create(airline=airline, **airplane_data)
        return airline
