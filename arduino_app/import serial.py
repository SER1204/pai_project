import serial
import time
import os
import django

# Setează variabilele de mediu pentru Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PAI_PROJECT.settings')
django.setup()

# Importă modelul de date din Django
from sensors.models import SensorData

# Conectează-te la Arduino (înlocuiește 'COM3' cu portul corect)
arduino = serial.Serial('COM4', 9600)
time.sleep(2)  # Așteaptă câteva secunde pentru a stabili conexiunea

while True:
    if arduino.in_waiting > 0:
        # Citește datele de la Arduino
        sensor_data = arduino.readline().decode('utf-8').strip()
        print(f"Received: {sensor_data}")

        # Procesăm datele pentru fiecare senzor
        try:
            # Extrage valorile senzorilor din mesajul primit
            values = sensor_data.split(', ')
            sensor1_value = int(values[0].split(': ')[1])
            sensor2_value = int(values[1].split(': ')[1])
            sensor3_value = int(values[2].split(': ')[1])

            # Salvează datele în baza de date
            SensorData.objects.create(sensor1_value=sensor1_value, sensor2_value=sensor2_value, sensor3_value=sensor3_value)

            print(f"Saved: Sensor1: {sensor1_value}, Sensor2: {sensor2_value}, Sensor3: {sensor3_value}")
        except Exception as e:
            print(f"Error processing data: {e}")

        # Așteaptă 1 secundă înainte de a citi din nou
        time.sleep(1)
