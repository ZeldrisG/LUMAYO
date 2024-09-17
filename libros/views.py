from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.sessions.models import Session


from libros.models import Genero, Libro
from libros.forms import Agregar_Libro_Form, GeneroForm

from usuarios.mixins import RootLoginMixin, AdminLoginMixin, ClienteLoginMixin


# Create your views here.
 

class Admin_Libro(AdminLoginMixin, TemplateView):
    template_name = 'libros/administrar-libro.html'



class Agregar_Libro(AdminLoginMixin, CreateView):
    model = Libro
    form_class = Agregar_Libro_Form
    template_name = 'libros/agregar-libro.html'
    success_url = reverse_lazy('libros:admin-libro')

    def get_context_data(self, **kwargs):
        context = super(Agregar_Libro, self).get_context_data(**kwargs)
        
        formulario = GeneroForm()
        context['form2'] = formulario
        return context

    def form_valid(self, form):
        libro = form.save(commit = False)
        genero = GeneroForm(self.request.POST)
        aux = genero.save(commit=False)
        aux.save()
        libro.genero = aux
        libro.save()
        return super().form_valid(form)


class Listar_Libro(AdminLoginMixin, ListView):
    model = Libro
    template_name = 'libros/listar-libro.html'
    ordering = ["id"]


class Editar_Libro(AdminLoginMixin, UpdateView):
    model = Libro
    form_class = Agregar_Libro_Form
    template_name = 'libros/actualizar-libro.html'
    success_url = reverse_lazy('libros:listar-libro')

    def get_context_data(self, **kwargs):
        context = super(Editar_Libro, self).get_context_data(**kwargs)
        libro = self.get_object()
        form2 = GeneroForm(instance= libro.genero)
        context['form2'] = form2
        return context

    def form_valid(self, form):
        libro = form.save(commit = False)
        genero = GeneroForm(self.request.POST)
        aux = genero.save(commit=False)
        aux.save()
        libro.genero = aux
        libro.save()
        return super().form_valid(form)


class Eliminar_Libro(AdminLoginMixin, DeleteView):
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

    def get_context_data(self, **kwargs):
        context = super(Post_Libro, self).get_context_data(**kwargs)
        libro = self.get_object()
        form2 = GeneroForm(instance= libro.genero)
        context['form2'] = form2
        return context



