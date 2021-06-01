from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, TemplateView

from reserva.models import Reserva

# Create your views here.
class Agregar_Reserva(TemplateView):
    model = Reserva
    template_name = 'libros/agregar-reserva.html'

    def get(self, request, *args, **kwargs):
        libro = Libro.objects.all()
        reserva = self.model.objects.all()

        libro = self.model.objects.all()
        busqueda = self.request.GET.get("buscar")
        if busqueda:
            object_list = libro.filter(
                    Q(issn__icontains = busqueda) |
                    Q(titulo__icontains = busqueda) |
                    Q(autor__icontains = busqueda) |
                    Q(editorial__icontains = busqueda)
                ).distinct()

            context = {
                'object_list' : object_list
            }
            return object_list
        return render(request, "index.html")