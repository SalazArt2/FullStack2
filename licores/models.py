from django.db import models
from django.urls import reverse
import uuid 
from django.contrib.auth import get_user_model

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=30)
    relacionadas = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='relacionadas_con')

    def __str__(self):
        return self.categoria

    

class Licor( models.Model ):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    imagen=models.ImageField(upload_to='imagenes/',blank=True)
    descripcion = models.CharField(max_length=200)
    categorias = models.ManyToManyField(Categoria, related_name="licores")

    class Meta:
        permissions=[
            ('special_status','Puede ver todos los licores')
        ]

    def __str__( self ):
        return self.nombre

    def get_absolute_url( self ):
        return reverse( "detalle_licor", args=[str(self.id)] )
    
class Resenha(models.Model):
    licor = models.ForeignKey(
        Licor,
        on_delete=models.CASCADE,
        related_name="resenhas"
    )
    resenha=models.CharField(max_length=255)
    autor=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__ (self):
        return self.resenha

