from django import forms
from .models import Resenha,Licor

class ResenhaForm(forms.ModelForm):
    class Meta:
        model = Resenha
        fields = ['resenha']

class LicorForm(forms.ModelForm):
    class Meta:
        model = Licor
        fields = ['nombre', 'marca', 'cantidad', 'descripcion', 'precio', 'imagen', 'categorias']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categorias': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

