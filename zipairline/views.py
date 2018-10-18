from rest_framework import generics
from .serializers import ZipAirplaneSerializer
from .models import ZipAirplane


class ZipAirlineList(generics.ListCreateAPIView):
    queryset = ZipAirplane.objects.all()
    serializer_class = ZipAirplaneSerializer


class ZipAirlineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ZipAirplane.objects.all()
    serializer_class = ZipAirplaneSerializer
