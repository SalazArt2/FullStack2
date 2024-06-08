from django.contrib import admin
from .models import Licor,Resenha,Categoria

admin.site.register(Categoria)

class ResenhaEnLinea(admin.TabularInline):
    model=Resenha

class LicorAdmin( admin.ModelAdmin ):
    inlines=(
        ResenhaEnLinea,
    )    
    list_display = ('nombre', 'marca', 'precio','descripcion')

# Register your models here.
admin.site.register( Licor, LicorAdmin )