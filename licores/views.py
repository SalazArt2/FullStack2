from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.db.models import Q,Count
from .models import Licor, Categoria

# Create your views here.
class VistaListaLicores(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Licor
    context_object_name = 'lista_licores'
    template_name = 'licores/lista_licores.html'
    login_url = 'account_login'
    permission_required = 'libros.special_status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.annotate(num_relacionadas=Count('relacionadas')).filter(num_relacionadas__gt=0)
        return context

class VistaLicoresFiltrados(ListView):
    model = Licor
    context_object_name = 'lista_licores'
    template_name = 'licores/licores_filtrados.html'

    def get_queryset(self):
        consulta = self.request.GET.get('filtro')
        consulta2 = self.request.GET.get('filtro2')
        if consulta:
            categoria = Categoria.objects.filter(categoria__icontains=consulta).first()
            if categoria:
                categorias_relacionadas = categoria.relacionadas.all()
                if consulta2:
                    subcategoria = Categoria.objects.filter(categoria__icontains=consulta2).first()
                    if subcategoria:
                        return Licor.objects.filter(categorias=subcategoria)
                return Licor.objects.filter(
                    Q(categorias=categoria) | Q(categorias__in=categorias_relacionadas)
                )
        return Licor.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener categorías que tienen al menos una categoría relacionada
        context['categorias'] = Categoria.objects.annotate(num_relacionadas=Count('relacionadas')).filter(num_relacionadas__gt=0)
        filtro = self.request.GET.get('filtro', '')
        filtro2 = self.request.GET.get('filtro2', '')
        context['filtro'] = filtro
        context['filtro2'] = filtro2

        if filtro:
            categoria = Categoria.objects.filter(categoria__icontains=filtro).first()
            if categoria:
                # Obtener solo las subcategorías de la categoría filtrada
                context['subcategorias'] = categoria.relacionadas.all()
            else:
                context['subcategorias'] = []
        else:
            context['subcategorias'] = []

        return context

class VistaDetalleLicor( DetailView ):
    model = Licor
    context_object_name = 'licor'
    template_name = 'licores/detalle_licor.html'

class VistaResultadosBusqueda(  ListView):
    model= Licor
    context_object_name = 'lista_licores'
    template_name = 'licores/resultados_busqueda.html'
    #queryset = Libro.objects.filter(Q(titulo__icontains='alba') | Q(titulo__icontains='web'))
    def get_queryset(self):
        consulta=self.request.GET.get('query')    
        return Licor.objects.filter(Q(nombre__icontains=consulta)|Q(marca__icontains=consulta))
