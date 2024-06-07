from django.urls import path

from .views import VistaPaginaRegistro

urlpatterns = [
    path( 'signup/', VistaPaginaRegistro.as_view(), name='signup' )
]