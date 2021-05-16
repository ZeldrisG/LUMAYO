from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, TemplateView
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
    success_url = reverse_lazy('libros:listar-libro')



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
