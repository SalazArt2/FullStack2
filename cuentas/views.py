from django.views import generic
from django.urls import reverse_lazy
from .forms import FormularioCreacionUsuario
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

# Create your views here.
class VistaPaginaRegistro( generic.CreateView ):
    form_class = FormularioCreacionUsuario
    success_url = reverse_lazy( 'login' )
    template_name = 'registration/signup.html'
    

class CustomPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset_form.html'
    email_template_name = 'account/password_reset_email.html'
    success_url = 'password_reset_done'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = 'password_reset_complete'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'