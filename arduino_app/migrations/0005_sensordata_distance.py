# Generated by Django 3.2 on 2024-11-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arduino_app', '0004_auto_20241125_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='distance',
            field=models.FloatField(default=0.0),
        ),
    ]
