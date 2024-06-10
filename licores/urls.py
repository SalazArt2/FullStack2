from django.urls import path
from .views import VistaListaLicores, VistaDetalleLicor, VistaResultadosBusqueda, VistaLicoresFiltrados, delete_resenha, profile_view, update_resenha,VistaCarrito,VistaAgregarAlCarrito, VistaVerWishlist, VistaAgregarAWishlist, VistaAgregarLicor

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('', VistaListaLicores.as_view(), name='lista_licores'),
    path('<uuid:pk>/', VistaDetalleLicor.as_view(), name='detalle_licor'),
    path('buscar/', VistaResultadosBusqueda.as_view(), name='resultados_busqueda'),
    path('filtro/', VistaLicoresFiltrados.as_view(), name='licores_filtrados'),
    path('delete_resenha/<int:pk>/', delete_resenha, name='delete_resenha'),
    path('update_resenha/', update_resenha, name='update_resenha'),
    path('carrito/', VistaCarrito.as_view(), name='carrito'),
    path('anhadir_carrito/', VistaAgregarAlCarrito.as_view(), name='anhadir_carrito'),
    path('wishlist/', VistaVerWishlist.as_view(), name='wishlist'),
    path('anhadir_wishlist/', VistaAgregarAWishlist.as_view(), name='anhadir_wishlist'),
    path('nuevo_licor/',VistaAgregarLicor.as_view(),name='nuevo_licor')
]
