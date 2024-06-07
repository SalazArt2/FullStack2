from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import VistaPaginaInicio

# Create your tests here.
class PruebasPaginaInicio( SimpleTestCase ):
    def setUp( self ):
        url = reverse( 'inicio' )
        self.respuesta = self.client.get( url )

    def test_url_existe_en_ubicacion_correcta( self ):
        self.assertEqual( self.respuesta.status_code, 200)

    def test_plantilla_pagina_inicio(self):
        self.assertTemplateUsed( self.respuesta, 'inicio.html')

    def test_pagina_incio_contiene_html_correcto( self ):
        self.assertContains( self.respuesta, 'página de inicio')

    def test_pagina_inicio_no_contiene_html_correcto( self ):
        self.assertNotContains( self.respuesta, 'Hola!! este texto no debería aparecer en la página')

    def test_url_pagina_inicio_resuelve_vista_pagina_inicio( self ):
        vista = resolve('/')
        self.assertEqual( vista.func.__name__, VistaPaginaInicio.as_view().__name__ )