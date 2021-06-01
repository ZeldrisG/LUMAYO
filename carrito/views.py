from django.shortcuts import redirect, render
from carrito.models import Carrito
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView, ListView, View
from django.views.generic.detail import DetailView
from carrito.forms import Agregar_Carrito_Form
from libros.models import Libro
from usuarios.models import Usuario


class Añadir_Carrito(TemplateView):
    template_name = 'carrito/carrito.html'

    def dispatch(self, request, *args, **kwargs):
        libro = Libro.objects.all()
        print(kwargs)
        consulta2 = Libro.objects.get(id = kwargs['pk'])
        usuario = Usuario.objects.all()
        usuario = Usuario.objects.get(username=self.request.user)
        consulta = Carrito.objects.get(usuario = usuario)
        if consulta:
            consulta.libros.add(consulta2)
            consulta.save()
        else:
            carrito = Carrito(usuario = usuario)
            consulta.libros.add(consulta2)
            carrito.save()

        return redirect('usuarios:login')

class Listar_Carrito(TemplateView):
    template_name = 'carrito/listar-carrito.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carrito = Carrito.objects.get(usuario_id = self.request.user.id)
        context['object_list'] = carrito.libros.all()
        return context


""" class Listar_Carrito(View):
    model = Carrito
    template_name = 'carrito/listar-carrito.html'

    def get(self, request, *args, **kwargs ):
        
        consulta = Carrito.objects.get(usuario_id = self.request.user.id)
        print(consulta)
        context = {'object_list':consulta}
        return consulta """
    








class Editar_Carrito(UpdateView):
    model = Carrito
    form_class = Agregar_Carrito_Form
    template_name = 'carrito/actualizar-carrito.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        
