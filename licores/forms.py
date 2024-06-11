from django import forms
from .models import Resenha,Licor

class ResenhaForm(forms.ModelForm):
    class Meta:
        model = Resenha
        fields = ['resenha']

class LicorForm(forms.ModelForm):
    class Meta:
        model = Licor
        fields = ['nombre', 'marca', 'cantidad','descripcion', 'precio', 'imagen', 'categorias']