from django.db import models
from drivers.models import Driver

# Create your models here.

class Vehicle(models.Model):
    LOCATION_CHOICES = [
        ('Rua', 'Rua'),
        ('Garagem', 'Garagem'),
        ('Manutencao', 'Manutenção'),
    ]
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    plate = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    current_location = models.CharField(max_length=100, default='garagem', choices=LOCATION_CHOICES)
    active = models.BooleanField(default=True)
