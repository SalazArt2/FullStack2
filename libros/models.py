from django.db import models
from django.urls import reverse
import uuid 
from django.contrib.auth import get_user_model

# Create your models here.
class Categoria(models.Model):
    categoria=models.CharField(max_length=30)
    def __str__ (self):
        return self.categoria
    

class Libro( models.Model ):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    portada=models.ImageField(upload_to='portadas/',blank=True)
    categorias = models.ManyToManyField(Categoria, related_name="libros")

    class Meta:
        permissions=[
            ('special_status','Puede leer todos los libros')
        ]

    def __str__( self ):
        return self.titulo

    def get_absolute_url( self ):
        return reverse( "detalle_libro", args=[str(self.id)] )
    
class Resegna(models.Model):
    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name="resegnas"
    )
    resegna=models.CharField(max_length=255)
    autor=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__ (self):
        return self.resegna

