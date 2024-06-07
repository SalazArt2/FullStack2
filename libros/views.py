from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.db.models import Q
from .models import Libro

# Create your views here.
class VistaListaLibros( PermissionRequiredMixin, LoginRequiredMixin, ListView ):
    model = Libro
    context_object_name = 'lista_libros'
    template_name = 'libros/lista_libros.html'
    login_url='account_login' 
    permission_required='libros.special_status'   

class VistaDetalleLibro( DetailView ):
    model = Libro
    context_object_name = 'libro'
    template_name = 'libros/detalle_libro.html'

class VistaResultadosBusqueda(  ListView):
    model= Libro
    context_object_name = 'lista_libros'
    template_name = 'libros/resultados_busqueda.html'
    #queryset = Libro.objects.filter(Q(titulo__icontains='alba') | Q(titulo__icontains='web'))
    def get_queryset(self):
        consulta=self.request.GET.get('query')    
        return Libro.objects.filter(Q(titulo__icontains=consulta)|Q(autor__icontains=consulta))
