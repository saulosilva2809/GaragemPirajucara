from django.shortcuts import render
from .models import Vehicle

# Create your views here.

def list_vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/list_vehicle.html', {'vehicles': vehicles})
