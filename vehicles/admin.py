from django.contrib import admin
from .models import Vehicle

# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('plate', 'model', 'brand', 'current_location', 'active')
    search_fields = ('plate', 'model', 'brand', 'year', 'active', 'current_location')
