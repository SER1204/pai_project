from django.shortcuts import render
from .models import SensorData

def sensor_data_view(request):
    # Preia toate datele din baza de date și le ordonează după timestamp (descrescător)
    sensor_data = SensorData.objects.all().order_by('-timestamp')
    
    # Transmite datele către șablon
    return render(request, 'sensor-data.html', {'sensor_data': sensor_data})
