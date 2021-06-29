from django.shortcuts import render
from django.views.generic.edit import CreateView

from perfiles_facturacion.models import PerfilFacturacion

# Create your views here.
 
class PerfilFacturacionCreateView(CreateView):
     model = PerfilFacturacion
     template_name = "perfiles_facturacion/crear.html"
 