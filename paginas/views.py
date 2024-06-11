import random
from django.views.generic import ListView
from licores.models import Licor

class VistaInicio(ListView):
    model = Licor
    template_name = 'inicio.html'
    context_object_name = 'licores'

    def get_queryset(self):
        licores = list(Licor.objects.all())
        if len(licores) > 6:
            licores = random.sample(licores, 6)
        return licores