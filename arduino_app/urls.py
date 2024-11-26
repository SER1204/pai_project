from django.urls import path
from .views import SensorDataAPIView

urlpatterns = [
    # Other URLs...
    path('api/sensor-data/', SensorDataAPIView.as_view(), name='sensor_data_api'),
]
