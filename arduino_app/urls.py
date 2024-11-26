from django.urls import path
from .views import sensor_data_view

urlpatterns = [
    path('sensor-data/', sensor_data_view, name='sensor-data'),
]
