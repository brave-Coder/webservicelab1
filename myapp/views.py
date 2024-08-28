from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .models import Temperature
from .serializer import TemperatureSerializer

def dashboard(request):
    return render(request, 'myapp/dashboard.html')

class TemperatureDetailView(generics.RetrieveAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class TemperatureListView(generics.ListAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class TemperatureCreateAPIView(generics.CreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

def get_latest_readings(request):
    latest_reading = Temperature.objects.latest('timestamp')
    data = {
        'temperature': latest_reading.temperature,
        'humidity': latest_reading.humidity
    }
    return JsonResponse(data)