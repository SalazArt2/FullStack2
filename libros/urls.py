from django.urls import path
from .views import VistaListaLibros, VistaDetalleLibro, VistaResultadosBusqueda

urlpatterns = [
    path('', VistaListaLibros.as_view(), name='lista_libros'),
    path('<uuid:pk>/', VistaDetalleLibro.as_view(), name='detalle_libro'),
    path('buscar/',VistaResultadosBusqueda.as_view(),name='resultados_busqueda'),
]