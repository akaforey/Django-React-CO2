from django.contrib import admin
from .models import CO2
# Register your models here.


class CO2Admin(admin.ModelAdmin):
    list_display = ('timestamp', 'co2_reading')

admin.site.register(CO2, CO2Admin)
