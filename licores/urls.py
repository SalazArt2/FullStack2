from django.urls import path
from .views import VistaListaLicores, VistaDetalleLicor, VistaResultadosBusqueda, VistaLicoresFiltrados, delete_resenha, profile_view, update_resenha

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('', VistaListaLicores.as_view(), name='lista_licores'),
    path('<uuid:pk>/', VistaDetalleLicor.as_view(), name='detalle_licor'),
    path('buscar/', VistaResultadosBusqueda.as_view(), name='resultados_busqueda'),
    path('filtro/', VistaLicoresFiltrados.as_view(), name='licores_filtrados'),
    path('delete_resenha/<int:pk>/', delete_resenha, name='delete_resenha'),
    path('update_resenha/', update_resenha, name='update_resenha'),
]
