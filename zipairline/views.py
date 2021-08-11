from rest_framework import generics
from .serializers import ZipAirplaneSerializer, ZipAirlinesSerializer
from .models import ZipAirplane, ZipAirline


class ZipAirplaneList(generics.ListCreateAPIView):
    queryset = ZipAirplane.objects.all()
    serializer_class = ZipAirplaneSerializer


class ZipAirplaneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ZipAirplane.objects.all()
    serializer_class = ZipAirplaneSerializer


class ZipAirlines(generics.ListCreateAPIView):
    queryset = ZipAirline.objects.all()
    serializer_class = ZipAirlinesSerializer
