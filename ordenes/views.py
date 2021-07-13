import threading
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from django.contrib import messages

from ordenes.models import Orden
from ordenes.forms import DevolucionesForm
from ordenes.utils import get_or_create_orden, breadcrumb, destruir_orden
from ordenes.mails import Mail
from ordenes.common import OrdenEstado
from envios.models import DireccionEnvio
from metodos_pago.models import Tarjeta
from libros.models import Libro
from carrito.utils import get_create_carrito, destruir_carrito
from usuarios.mixins import ClienteLoginMixin
# Create your views here.

class OrdenView(ClienteLoginMixin, View):
    template_name = 'ordenes/orden.html'
    model = Orden

    def get(self, request, *args, **kwargs):
        carrito = get_create_carrito(request)
        orden = get_or_create_orden(carrito, request)
        context = {
            'carrito' : carrito,
            'orden' : orden,
            'breadcrumb' : breadcrumb()
        }
        return render(request, self.template_name, context)

class Direccion(ClienteLoginMixin, View):
    template_name = 'ordenes/direccion.html'

    def get(self, request, *args, **kwargs):
        carrito = get_create_carrito(request)
        orden = get_or_create_orden(carrito, request)
        direccion = orden.get_or_set_direccion_envio()
        puede_elegir_direccion = DireccionEnvio.objects.filter(usuario=self.request.user).count() > 1
        context = {
            'carrito' : carrito,
            'orden' : orden,
            'breadcrumb' : breadcrumb(direccion=True),
            'direccion': direccion,
            'puede_elegir_direccion': puede_elegir_direccion
        }
        return render(request, self.template_name, context)

class SeleccionarDireccion(ClienteLoginMixin, View):
    template_name = 'ordenes/selecciona-direccion.html'
    model = DireccionEnvio
    def get(self, request, *args, **kwargs):
        direcciones = self.model.objects.filter(usuario=request.user)
        context = {
            'breadcrumb' : breadcrumb(direccion=True),
            'direcciones': direcciones
        }
        return render(request, self.template_name, context)

class EstablecerDireccion(ClienteLoginMixin, View):
    model = DireccionEnvio
    def get(self, request, *args, **kwargs):
        carrito = get_create_carrito(request)
        orden = get_or_create_orden(carrito, request)
        direccionEnvio = get_object_or_404(DireccionEnvio, pk=kwargs['pk'])

        if request.user.id != direccionEnvio.usuario_id:
            return redirect('carrito:miCarrito')

        orden.update_direccion_envio(direccionEnvio)
        return redirect('ordenes:direccion')




class Metodo_Pago(ClienteLoginMixin, View):
    template_name = 'ordenes/metodo_pago.html'

    def get(self, request, *args, **kwargs):
        carrito = get_create_carrito(request)
        orden = get_or_create_orden(carrito, request)
        metodo_pago = orden.get_or_set_metodo_pago()
        puede_elegir_tarjeta = Tarjeta.objects.filter(usuario=self.request.user).count() > 1
        direccionEnvio = orden.direccion_envio
        if direccionEnvio is None:
            return redirect('ordenes:direccion ')
        
        context = {
            'carrito': carrito,
            'orden': orden,
            'direccion': direccionEnvio,
            'tarjeta': metodo_pago,
            'breadcrumb' : breadcrumb(direccion=True, pago=True),
            'puede_elegir_tarjeta': puede_elegir_tarjeta
        }

        return render(request, self.template_name, context)


class SeleccionarTarjeta(ClienteLoginMixin, View):
    template_name = 'ordenes/selecciona-metodo_pago.html'
    model = Tarjeta
    def get(self, request, *args, **kwargs):
        metodos_pago = self.model.objects.filter(usuario=request.user)
        context = {
            'breadcrumb' : breadcrumb(direccion=True, pago=True),
            'tarjetas': metodos_pago
        }
        return render(request, self.template_name, context)


class EstablecerTarjeta(ClienteLoginMixin, View):
    model = Tarjeta
    def get(self, request, *args, **kwargs):
        carrito = get_create_carrito(request)
        orden = get_or_create_orden(carrito, request)
        tarjeta = get_object_or_404(Tarjeta, pk=kwargs['pk'])

        if request.user.id != tarjeta.usuario_id:
            return redirect('carrito:miCarrito')

        orden.update_metodo_pago(tarjeta)
        return redirect('ordenes:pago')


class Confirmacion(ClienteLoginMixin, View):

    template_name = 'ordenes/confirmacion.html'

    def get(self, request, *args, **kwargs):
        carrito = get_create_carrito(request)
        orden = get_or_create_orden(carrito, request)

        direccionEnvio = orden.direccion_envio
        if direccionEnvio is None:
            return redirect('ordenes:direccion ')

        tarjeta = orden.metodo_pago
        if tarjeta is None:
            return redirect('ordenes:pago ')
        saldo = tarjeta.saldo.compare(orden.get_total())
        if saldo.is_signed():
            messages.error(request, 'Saldo insuficiente en metodo de pago seleccionado...')
            return redirect('ordenes:pago')
        
        context = {
            'carrito': carrito,
            'orden': orden,
            'direccion': direccionEnvio,
            'tarjeta': tarjeta,
            'breadcrumb' : breadcrumb(direccion=True, pago=True, confirmacion=True),
        }

        return render(request, self.template_name, context)


class Cancelar(ClienteLoginMixin, View):
    
    def get(self, request, *args, **kwargs):
        carrito = get_create_carrito(request)
        orden = get_or_create_orden(carrito, request)

        if request.user.id != orden.usuario_id:
            return redirect('carrito:miCarrito')

        orden.cancelar()

        destruir_carrito(request)
        destruir_orden(request)
        
        messages.error(request, 'Orden de compra cancelada...')
        return redirect('inicio')


class Completar(ClienteLoginMixin, View):
    
    def get(self, request, *args, **kwargs):
        carrito = get_create_carrito(request)
        orden = get_or_create_orden(carrito, request)
        tarjeta = orden.metodo_pago
        metodo_pago = Tarjeta.objects.get(pk=tarjeta.pk)
        metodo_pago.actualizar_saldo(-orden.get_total())
        libros = carrito.libros_relacionados()

        if request.user.id != orden.usuario_id:
            return redirect('carrito:miCarrito')

        for item in libros:
            libro = Libro.objects.get(pk=item.libro.pk)
            libro.actualizar_existencias(-item.cantidad)

        

        orden.completar()

        hilo = threading.Thread(target=Mail.send_orden_completada, args=(orden, request.user))

        hilo.start()
        
        
        destruir_carrito(request)
        destruir_orden(request)
        
        messages.success(request, 'Orden de compra completada exitosamente...')
        return redirect('inicio')


class OrdenesListView(ListView):
    model = Orden
    template_name = "ordenes/lista-ordenes.html"

    def get_queryset(self):
        queryset = self.model.objects.filter(usuario_id=self.request.user.id).filter(estado=OrdenEstado.COMPLETADO)
        return queryset
    



class Devoluciones(View):
    template_name = 'ordenes/devoluciones.html'
    model = Orden
    def get(self, request, *args, **kwargs):
        queryset = self.model.objects.filter(usuario_id=self.request.user.id).filter(estado=OrdenEstado.COMPLETADO)
        context = {
            'orden' : queryset
        }
        return render(request, self.template_name, context)
