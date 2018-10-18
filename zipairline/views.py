from rest_framework import generics
from .serializers import ZipAirlineSerializer
from .models import ZipAirline


class ZipAirlineList(generics.ListCreateAPIView):
    queryset = ZipAirline.objects.all()
    serializer_class = ZipAirlineSerializer


class ZipAirlineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ZipAirline.objects.all()
    serializer_class = ZipAirlineSerializer
