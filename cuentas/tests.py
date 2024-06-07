from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import FormularioCreacionUsuario
from .views import VistaPaginaRegistro

class SignUpPageTest( TestCase ):
    def setUp( self ):
        url = reverse( "signup" )
        self.response = self.client.get( url )

    def test_signup_template( self ):
        self.assertEqual( self.response.status_code, 200 )

        self.assertTemplateUsed( self.response, "registration/signup.html" )
        self.assertTemplateNotUsed( self.response, "Hi there I should not be on the page" )

    def test_signup_form( self ):
        form = self.response.context.get( "form" )
        self.assertIsInstance( form, FormularioCreacionUsuario )
        self.assertContains( self.response, "csrfmiddlewaretokken" )

    def test_signup_view( self ):
        view = resolve( "cuentas/signup/" )
        self.assertEqual( view.func.__name__, VistaPaginaRegistro.as_view().__name__ )

# Create your tests here.
class PruebasUsuarios( TestCase ):
    def test_crear_usuario( self ):
        Usuario = get_user_model()
        usuario = Usuario.objects.create_user(
            username = 'Cesar',
            email = 'cesar@correo.itlalaguna.edu.mx',
            password = 'contraseñasecreta'
        )

        self.assertEqual( usuario.username, 'Cesar' )
        self.assertEqual( usuario.email, 'cesar@correo.itlalaguna.edu.mx' )
        self.assertTrue( usuario.is_active )
        self.assertFalse( usuario.is_staff )
        self.assertFalse( usuario.is_superuser )

    def test_crear_superusuario( self ):
        Usuario = get_user_model()
        usuario_admin = Usuario.objects.create_superuser(
            username = 'superadmin', 
            email = 'superadmin@correo.itlalaguna.edu.mx', 
            password = 'contraseñasecreta'
        )

        self.assertEqual( usuario_admin.username, 'superadmin' )
        self.assertEqual( usuario_admin.email, 'superadmin@correo.itlalaguna.edu.mx' )
        self.assertTrue( usuario_admin.is_active )
        self.assertTrue( usuario_admin.is_staff )
        self.assertTrue( usuario_admin.is_superuser )

