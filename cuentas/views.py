from django.views import generic
from django.urls import reverse_lazy
from .forms import FormularioCreacionUsuario

# Create your views here.
class VistaPaginaRegistro( generic.CreateView ):
    form_class = FormularioCreacionUsuario
    success_url = reverse_lazy( 'login' )
    template_name = 'registration/signup.html'