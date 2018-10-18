from rest_framework.serializers import ModelSerializer
from .models import ZipAirline


class ZipAirlineSerializer(ModelSerializer):

    class Meta:
        model = ZipAirline
        fields = ('zipairline_id', 'passenger_numb')