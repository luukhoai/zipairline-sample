from rest_framework import generics
from rest_framework.response import Response
from .serializers import ZipAirplaneSerializer, ZipAirlinesSerializer
from .models import ZipAirplane
from rest_framework.views import APIView


class ZipAirplaneList(generics.ListCreateAPIView):
    queryset = ZipAirplane.objects.all()
    serializer_class = ZipAirplaneSerializer


class ZipAirplaneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ZipAirplane.objects.all()
    serializer_class = ZipAirplaneSerializer


class ZipAirlines(APIView):

    def post(self, request, format=None):
        """Post ZipAirlines data"""

        # Verify data follow
        dict_data = dict(request.data)
        airline_id = int(dict_data['airline_id'][0])
        airline_name = dict_data['airline_name'][0]

        data = {
            'airline_id': airline_id,
            'airline_name': airline_name,
            'airplanes': []}
        for airplane in dict(request.data)['airplanes']:
            airplane = eval(airplane)
            airplane['airline'] = airline_id
            data['airplanes'].append(airplane)

        airlines = ZipAirlinesSerializer(data=data)
        if airlines.is_valid(raise_exception=True):
            airlines.save()
            return Response(airlines.data)
