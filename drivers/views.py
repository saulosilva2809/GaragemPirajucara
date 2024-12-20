from django.shortcuts import render, redirect, get_object_or_404
from .models import Driver
from .forms import CreateUpdateDriversForm

# Create your views here.

def list_drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/list_drivers.html', {'drivers': drivers})

def create_driver(request):
    if request.method == 'POST':
        form = CreateUpdateDriversForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_drivers')
    else:
        form = CreateUpdateDriversForm()
    return render(request, 'drivers/create_driver.html', {'form': form})

def update_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    if request.method == 'POST':
        form = CreateUpdateDriversForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('list_drivers')
    else:
        form = CreateUpdateDriversForm(instance=driver)
    return render(request, 'drivers/update_driver.html', {'form': form})

def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    driver.delete()
    return redirect('list_drivers')
