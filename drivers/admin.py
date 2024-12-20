from django.contrib import admin
from .models import Driver

# Register your models here.

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'number_cnh', 'category_cnh', 'phone', 'active')
    search_fields = ('name', 'cpf', 'number_cnh', 'category_cnh', 'phone', 'active')
