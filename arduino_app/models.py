from django.db import models

class SensorData(models.Model):
    temperature = models.FloatField(default=0.0)  # For temperature
    potentiometer = models.IntegerField()  # For potentiometer value
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when entry is created
    distance = models.FloatField(default=0.0)  # Asigură-te că este FloatField

    def __str__(self):
        return f"Temp: {self.temperature} C, Pot: {self.potentiometer}"

    def save(self, *args, **kwargs):
        # Call the superclass save method to actually save the data
        super().save(*args, **kwargs)

        # If there are more than 10 entries, delete the oldest one
        if SensorData.objects.count() > 5:
            oldest_entry = SensorData.objects.order_by('timestamp').first()  # Get the oldest entry
            oldest_entry.delete()  # Delete the oldest entry

#modificare