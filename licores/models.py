from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=30)
    relacionadas = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='relacionadas_con')

    def __str__(self):
        return self.categoria

class Licor(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes/', blank=True)
    cantidad = models.PositiveIntegerField(default=100)
    descripcion = models.CharField(max_length=200)
    categorias = models.ManyToManyField(Categoria, related_name="licores")

    creador = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        permissions = [
            ('special_status', 'Puede ver todos los licores')
        ]

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("detalle_licor", args=[str(self.id)])

    def get_editable_url(self):
        return reverse("editar_licor", args=[str(self.id)])

    def get_default_user():
        User = get_user_model()
        return User.objects.first().id if User.objects.exists() else None

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes/', blank=True)
    cantidad = models.PositiveIntegerField(default=100)
    descripcion = models.CharField(max_length=200)
    categorias = models.ManyToManyField(Categoria, related_name="licores")

    creador = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=get_default_user,
    )

    class Meta:
        permissions = [
            ('special_status', 'Puede ver todos los licores')
        ]

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("detalle_licor", args=[str(self.id)])

    def get_editable_url(self):
        return reverse("editar_licor", args=[str(self.id)])

class Resenha(models.Model):
    licor = models.ForeignKey(
        Licor,
        on_delete=models.CASCADE,
        related_name="resenhas"
    )
    resenha = models.CharField(max_length=255)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.resenha

class Carrito(models.Model):
    usuario = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='carrito'
    )

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(
        Carrito,
        on_delete=models.CASCADE,
        related_name='items'
    )
    licor = models.ForeignKey(
        Licor,
        on_delete=models.CASCADE
    )
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.licor.nombre}"

class Wishlist(models.Model):
    usuario = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='wishlist'
    )

    def __str__(self):
        return f"Wishlist de {self.usuario.username}"

class ItemWishlist(models.Model):
    wishlist = models.ForeignKey(
        Wishlist,
        on_delete=models.CASCADE,
        related_name='items'
    )
    licor = models.ForeignKey(
        Licor,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Deseo un - {self.licor.nombre}"
