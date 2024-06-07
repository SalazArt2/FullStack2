from django.contrib import admin
from .models import Libro,Resegna,Categoria

admin.site.register(Categoria)

class ResegnaEnLinea(admin.TabularInline):
    model=Resegna

class LibroAdmin( admin.ModelAdmin ):
    inlines=(
        ResegnaEnLinea,
    )    
    list_display = ('titulo', 'autor', 'precio')

# Register your models here.
admin.site.register( Libro, LibroAdmin )