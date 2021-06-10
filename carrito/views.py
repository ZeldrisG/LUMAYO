from django.shortcuts import redirect, render
from carrito.models import Carrito
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, View
from django.views.generic.detail import DetailView
from carrito.forms import Agregar_Carrito_Form
from libros.models import Libro
from usuarios.models import Usuario
from django.urls import reverse_lazy


class Añadir_Carrito(TemplateView):
    template_name = 'carrito/carrito.html'

    def dispatch(self, request, *args, **kwargs):
        carrito_existe = Carrito.objects.filter(usuario_id = request.user.id).count() > 0
        consulta2 = Libro.objects.get(id = kwargs['pk'])
        print(consulta2)
        usuario = Usuario.objects.all()
        usuario = Usuario.objects.get(username=self.request.user)
        

        if carrito_existe:
            consulta = Carrito.objects.get(usuario = usuario)
            print(consulta2)
            consulta.libros.add(consulta2)
            consulta.save()
        else:
            carrito = Carrito(usuario = usuario)
            carrito.save()
            carrito.libros.add(consulta2)
            

        return redirect('carrito:listar-carrito')

class Listar_Carrito(TemplateView):
    template_name = 'carrito/listar-carrito.html'
    def get_context_data(self, **kwargs):
        carrito_existe = Carrito.objects.filter(usuario_id = self.request.user.id).count() > 0
        context = super().get_context_data(**kwargs)
        if carrito_existe:
            carrito = Carrito.objects.get(usuario_id = self.request.user.id)
            context['object_list'] = carrito.libros.all()
        
        else:
            context['object_list'] = False
        return context


class Eliminar_Libro_Carrito(TemplateView):
    template_name = 'carrito/carrito.html'
    def dispatch(self, request, *args, **kwargs):
        libro = Libro.objects.all()
        print(kwargs)
        consulta2 = Libro.objects.get(id = kwargs['pk'])
        usuario = Usuario.objects.all()
        usuario = Usuario.objects.get(username=self.request.user)
        consulta = Carrito.objects.get(usuario = usuario)
        if consulta:
            consulta.libros.remove(consulta2)

        return redirect('carrito:listar-carrito')


""" class Listar_Carrito(View):
    model = Carrito
    template_name = 'carrito/listar-carrito.html'

    def get(self, request, *args, **kwargs ):
        
        consulta = Carrito.objects.get(usuario_id = self.request.user.id)
        print(consulta)
        context = {'object_list':consulta}
        return consulta """
    


        
