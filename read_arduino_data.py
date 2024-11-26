import serial
import time
import os
import django

# Setează variabilele de mediu pentru Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PAI_PROJECT.settings')
django.setup()

# Importă modelul Django
from arduino_app.models import SensorData

# Conectează-te la Arduino (înlocuiește 'COM4' cu portul corect)
arduino = serial.Serial('COM4', 9600)
time.sleep(2)  # Așteaptă câteva secunde pentru stabilirea conexiunii

while True:
    try:
        if arduino.in_waiting > 0:
            # Citește linia trimisă de Arduino
            line = arduino.readline().decode('utf-8').strip()
            print(f"Received: {line}")

            # Analizează datele primite
            if line.startswith("Temperature:"):
                # Extrage valoarea temperaturii
                temperature = float(line.split(":")[1].strip().replace("C", "").strip())

            elif line.startswith("Potentiometer Value:"):
                # Extrage valoarea potențiometrului
                potentiometer = int(line.split(":")[1].strip())

                # Salvează în baza de date doar când avem ambele valori
                SensorData.objects.create(
                    temperature=temperature,
                    potentiometer=potentiometer
                )
                print(f"Saved data: Temp={temperature} C, Potentiometer={potentiometer}")

    except Exception as e:
        print(f"Error reading from Arduino: {e}")

    # Pauză de 100ms între citiri
    time.sleep(0.1)
