from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SensorData
from .serializers import SensorDataSerializer

class SensorDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Fetch the latest 10 records
        sensor_data = SensorData.objects.all().order_by('-timestamp')[:10]
        serializer = SensorDataSerializer(sensor_data, many=True)
        return Response(serializer.data)
