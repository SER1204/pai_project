# Generated by Django 3.2 on 2024-11-24 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arduino_app', '0002_sensordata_sensor4_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='sensor4_value',
        ),
    ]
