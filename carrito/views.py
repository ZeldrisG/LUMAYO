from django.shortcuts import render
from carrito.models import Carrito
from django.views.generic.edit import UpdateView
from carrito.forms import Agregar_Carrito_Form

class Editar_Carrito(UpdateView):
    model = Carrito
    form_class = Agregar_Carrito_Form
    template_name = 'carrito/actualizar-carrito.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
