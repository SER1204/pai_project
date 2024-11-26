# sensors/models.py
from django.db import models

class Sensor(models.Model):
    sensor_type = models.CharField(max_length=100)  # Tipul senzorului (ex: temperatură, umiditate)
    location = models.CharField(max_length=100)  # Locul unde se află senzorul (ex: birou, depozit)
    value = models.FloatField()  # Valoarea măsurată de senzor (ex: temperatura în grade Celsius)
    timestamp = models.DateTimeField(auto_now_add=True)  # Timpul când a fost citit senzorul

    def __str__(self):
        return f"{self.sensor_type} - {self.location} - {self.value}"
