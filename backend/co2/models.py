from django.db import models

# Create your models here.

class SensorReading(models.Model):
    timestamp = models.DateTimeField()
    co2_reading = models.PositiveIntegerField()

    def _str_(self):
        return f'{timestamp}, {co2_reading}'
