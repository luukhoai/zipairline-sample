import json
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
        print(request.data)
        data = json.dumps(request.data)
        print(data)
        airlines = ZipAirlinesSerializer(data=request.data)
        if airlines.is_valid(raise_exception=True):
            airlines.save()
            return Response(airlines.data)