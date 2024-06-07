from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import FormularioCreacionUsuario, FormularioCambiarUsuario

Usuario = get_user_model()

class UsuarioAdmin( UserAdmin ):
    add_form = FormularioCreacionUsuario
    form = FormularioCambiarUsuario
    model = Usuario
    list_display = [
        'email',
        'username',
        'is_superuser',
    ]

# Register your models here.
admin.site.register( Usuario, UserAdmin )