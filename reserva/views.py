from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseNotFound
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, TemplateView, View
import json
from datetime import datetime


from reserva.models import Reserva, ReservaLibros
from libros.models import Libro

# Create your views here.
class Agregar_Reserva(TemplateView):
    model = Reserva

    def post(self, request, *args, **kwargs):
        reserva_existe = self.model.objects.filter(usuario_id = request.user.id).count() > 0
        print(reserva_existe)
        datos = json.loads(request.body.decode("utf-8"))
        libro = Libro.objects.get(id=datos)
        miFecha = datetime.now()
        fechaFormateada = miFecha.strftime("%Y-%m-%d %H:%M:%S")

        if reserva_existe:
            reserva = self.model.objects.get(usuario_id=request.user.id)
            reserva.libros.add(
                libro,
                through_defaults={
                'fec_reserva' : fechaFormateada,
                'cantidad' : 1
                })
            return JsonResponse({'reserva':'true'})
        else:
            reserva = self.model(usuario_id=request.user.id)
            reserva.save()
            reserva.libros.add(
                libro,
                through_defaults={
                'fec_reserva' : fechaFormateada,
                'cantidad' : 1
                })
            print('error usuario no tiene reserva')
            return JsonResponse({'reserva':'false'})


class Mis_Reservas(TemplateView):
    model = ReservaLibros
    template_name = 'reserva/mis-reservas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reserva = Reserva.objects.get(usuario_id=self.request.user.id)
        context['object'] = reserva.reservalibros_set.all()
        return context

class Eliminar_Reserva(View):

    def post(self, request, *args, **kwargs):
        reserva = Reserva.objects.get(usuario_id=self.request.user.id)
        datos = json.loads(request.body.decode("utf-8"))
        try:
            libro = Libro.objects.get(id=datos)                                                                                                                                                                            
            reserva.libros.remove(libro)                                                                                      
            return JsonResponse({'estado': 'Reserva cancelada con exito!...'})                                                                          
        except:
            return JsonResponse({'estado': 'La reserva no ha podido ser cancelada!...'})                                                                          
