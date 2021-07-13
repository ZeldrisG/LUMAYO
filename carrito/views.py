from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, View
from django.urls import reverse_lazy

from libros.models import Libro
from usuarios.models import Usuario
from carrito.models import CarritoCompras, CarritoLibros
from carrito.utils import get_create_carrito

class CarritoView(TemplateView):
    template_name = 'carrito/carrito-view.html'
    model = CarritoCompras
    
    def get(self, request, *args, **kwargs):
        carrito = get_create_carrito(request)
        return render(request, self.template_name, {'object_list': carrito})

class Agregar_Carrito(View):
    template_name = 'carrito/agregar.html'
    
    def post(self, request, *args, **kwargs):
        carrito = get_create_carrito(request)
        libro = get_object_or_404(Libro, pk=request.POST.get('libroId'))
        cantidad = int(request.POST.get('cantidad', 1))

        carritolibros = CarritoLibros.objects.create_or_update_cantidad(
            carrito=carrito,
            libro=libro,
            cantidad=cantidad
            )
        context = {
            'libro': libro,
            'cantidad': cantidad
            }
        return render(request, self.template_name, context)

class EliminarLibro_Carrito(View):
    template_name = 'carrito/agregar.html'
    
    def post(self, request, *args, **kwargs):
        carrito = get_create_carrito(request)
        libro = get_object_or_404(Libro, pk=request.POST.get('libroId'))
        carrito.libros.remove(libro)
        return redirect('carrito:miCarrito')