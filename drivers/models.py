from django.db import models

# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=17, unique=True)
    number_cnh = models.CharField(max_length=20)
    category_cnh = models.CharField(max_length=2)
    phone = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

def __str__(self):
    return self.name
