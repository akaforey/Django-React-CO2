from django.contrib import admin
from .models import SensorReading
# Register your models here.


class SensorReadingAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'co2_reading')

admin.site.register(SensorReading, SensorReadingAdmin)
