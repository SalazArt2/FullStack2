from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q, Count
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from .models import Licor, Categoria, Resenha
from .forms import ResenhaForm

@login_required
def profile_view(request):
    return render(request, 'account/profile.html', {'user': request.user})

class VistaListaLicores(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Licor
    context_object_name = 'lista_licores'
    template_name = 'licores/lista_licores.html'
    login_url = 'account_login'
    permission_required = 'licores.special_status'

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
                        return Licor.objects.filter(categorias=subcategoria).distinct()
                return Licor.objects.filter(
                    Q(categorias=categoria) | Q(categorias__in=categorias_relacionadas)
                ).distinct()
        return Licor.objects.all().distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.annotate(num_relacionadas=Count('relacionadas')).filter(num_relacionadas__gt=0)
        filtro = self.request.GET.get('filtro', '')
        filtro2 = self.request.GET.get('filtro2', '')
        context['filtro'] = filtro
        context['filtro2'] = filtro2

        if filtro:
            categoria = Categoria.objects.filter(categoria__icontains=filtro).first()
            if categoria:
                context['subcategorias'] = categoria.relacionadas.all()
            else:
                context['subcategorias'] = []
        else:
            context['subcategorias'] = []

        return context

class VistaDetalleLicor(FormMixin, DetailView):
    model = Licor
    context_object_name = 'licor'
    template_name = 'licores/detalle_licor.html'
    form_class = ResenhaForm

    def get_success_url(self):
        return self.request.path

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'success': False, 'error': 'Not authenticated'})

        self.object = self.get_object()
        form = self.get_form()
        resenha_id = request.POST.get('resenha_id')

        if resenha_id:
            resenha = get_object_or_404(Resenha, id=resenha_id)
            if resenha.autor != request.user:
                return JsonResponse({'success': False, 'error': 'Not authorized'})
            resenha.resenha = form.cleaned_data['resenha']
            resenha.save()
            return JsonResponse({'success': True})
        else:
            if form.is_valid():
                resenha = form.save(commit=False)
                resenha.licor = self.object
                resenha.autor = request.user
                resenha.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': form.errors})

def delete_resenha(request, pk):
    if request.method == 'DELETE':
        resenha = get_object_or_404(Resenha, pk=pk)
        if request.user == resenha.autor:
            resenha.delete()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Not authorized'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def update_resenha(request):
    if request.method == 'POST':
        resenha_id = request.POST.get('resenha_id')
        resenha = get_object_or_404(Resenha, pk=resenha_id)
        if request.user == resenha.autor:
            resenha_text = request.POST.get('resenha')
            resenha.resenha = resenha_text
            resenha.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Not authorized'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

class VistaResultadosBusqueda(ListView):
    model = Licor
    context_object_name = 'lista_licores'
    template_name = 'licores/resultados_busqueda.html'
    
    def get_queryset(self):
        consulta = self.request.GET.get('query', '')
        return Licor.objects.filter(Q(nombre__icontains=consulta) | Q(marca__icontains=consulta))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '')
        return context
