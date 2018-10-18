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
        airlines = ZipAirlinesSerializer(data=request.data)
        if airlines.is_valid(raise_exception=True):
            return Response(airlines.data)