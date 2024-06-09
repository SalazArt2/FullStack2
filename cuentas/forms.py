from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from licores.models import Resenha 

class FormularioCreacionUsuario(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
        )

class FormularioCambiarUsuario(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
        )

class ResenhaForm(forms.ModelForm):
    class Meta:
        model = Resenha
        fields = ['resenha']
        widgets = {
            'resenha': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu reseña aquí...'}),
        }
