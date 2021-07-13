from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.sessions.models import Session


from libros.models import Libro
from libros.forms import Agregar_Libro_Form

# Create your views here.
 

class Admin_Libro(TemplateView):
    template_name = 'libros/administrar-libro.html'



class Agregar_Libro(CreateView):
    model = Libro
    form_class = Agregar_Libro_Form
    template_name = 'libros/agregar-libro.html'
    success_url = reverse_lazy('libros:admin-libro')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Listar_Libro(ListView):
    model = Libro
    template_name = 'libros/listar-libro.html'
    ordering = ["id"]


class Editar_Libro(UpdateView):
    model = Libro
    form_class = Agregar_Libro_Form
    template_name = 'libros/actualizar-libro.html'
    success_url = reverse_lazy('libros:listar-libro')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Eliminar_Libro(DeleteView):
    model = Libro
    template_name = 'libros/eliminar-libro.html'
    success_url = reverse_lazy('libros:listar-libro')


class Buscar_Libro(ListView):
    model = Libro
    template_name = 'libros/search.html'
    success_url = reverse_lazy('libros:search')

    def get_queryset(self):
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


class Post_Libro(DetailView):
    model = Libro
    template_name = 'libros/post-libro.html'



