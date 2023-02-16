from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SensorReadingSerializer
from .models import SensorReading


# Create your views here.
class SensorReadingView(viewsets.ModelViewSet):
    serializer_class = SensorReadingSerializer
    queryset = SensorReading.objects.all()
    