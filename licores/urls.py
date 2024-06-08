from django.urls import path
from .views import VistaListaLicores, VistaDetalleLicor, VistaResultadosBusqueda,VistaLicoresFiltrados

urlpatterns = [
    path('', VistaListaLicores.as_view(), name='lista_licores'),
    path('<uuid:pk>/', VistaDetalleLicor.as_view(), name='detalle_licor'),
    path('buscar/',VistaResultadosBusqueda.as_view(),name='resultados_busqueda'),
    path('filtro/',VistaLicoresFiltrados.as_view(),name='licores_filtrados'),
]