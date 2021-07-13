from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseNotFound
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, TemplateView, View

import json
from datetime import datetime


from reserva.models import Reserva, ReservaLibros
from libros.models import Libro
from reserva.utils import get_or_create_reserva

# Create your views here.
class Agregar_Reserva(TemplateView):
    model = Reserva
    template_name = 'reserva/agregar.html'
    def post(self, request, *args, **kwargs):
        reserva = get_or_create_reserva(request)
        libro = get_object_or_404(Libro, pk=request.POST.get('libroIdReserva'))
        cantidad = int(request.POST.get('cantidadReserva', 1))

        reservalibros = ReservaLibros.objects.create(
            reserva=reserva,
            libro=libro,
            cantidad=cantidad
            )
        context = {
            'libro': libro,
            'cantidad': cantidad
            }
        return render(request, self.template_name, context)


class Mis_Reservas(TemplateView):
    model = Reserva
    template_name = 'reserva/mis-reservas.html'

    def get(self, request, *args, **kwargs):
        reserva = get_or_create_reserva(request)
        return render(request, self.template_name, {'reserva': reserva})

class Eliminar_Reserva(View):
    
    def post(self, request, *args, **kwargs):
        reserva = get_or_create_reserva(request)
        libro = get_object_or_404(Libro, pk=request.POST.get('libroId'))
        reserva.libros.remove(libro)
        return redirect('reserva:mis-reservas')