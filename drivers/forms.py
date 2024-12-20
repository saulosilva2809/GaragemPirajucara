from django import forms
from .models import Driver

class CreateUpdateDriversForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'cpf', 'number_cnh', 'category_cnh', 'phone', 'active']
