from django.contrib import admin
from .models import Licor,Resenha,Categoria, Carrito, ItemCarrito,Wishlist,ItemWishlist

admin.site.register(Categoria)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(Wishlist)
admin.site.register(ItemWishlist)

class ResenhaEnLinea(admin.TabularInline):
    model=Resenha

class LicorAdmin( admin.ModelAdmin ):
    inlines=(
        ResenhaEnLinea,
    )    
    list_display = ('nombre', 'marca', 'precio','descripcion')

# Register your models here.
admin.site.register( Licor, LicorAdmin )