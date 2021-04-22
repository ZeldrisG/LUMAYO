from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from libros.models import Libro
from libros.forms import AddLibroForm

# Create your views here.

def admin_libro(request):
    
    return render(request, "libros/administrar-libro.html")

class add_libro(CreateView):
    model = Libro
    form_class = AddLibroForm
    template_name = 'libros/agregar-libro.html'
    success_url = reverse_lazy('admin_libro')
    
