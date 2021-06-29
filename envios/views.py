from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from envios.models import  DireccionEnvio
from envios.forms import DireccionEnvioForm
from carrito.utils import get_create_carrito
from ordenes.utils import get_or_create_orden
# Create your views here.

class DireccionesEnvioListView(ListView):
    model = DireccionEnvio
    template_name = 'envios/direcciones.html'

    def get_queryset(self):
        return self.model.objects.filter(usuario=self.request.user).order_by('-defecto')

class AgregarDireccion(SuccessMessageMixin, CreateView):
    model = DireccionEnvio
    form_class = DireccionEnvioForm
    template_name = 'envios/crear-direccion.html'
    success_url = reverse_lazy('envios:direcciones-envio')
    success_message = "%(direccion1) ha sido creado exitosamente..."

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.defecto = not self.model.objects.filter(usuario=self.request.user).exists()
        self.object.save()
        if self.request.GET.get('next'):
            self.next()
        return super().form_valid(form)
    
    def next(self):
        if self.request.GET['next'] == reverse('ordenes:direccion'):
            carrito = get_create_carrito(self.request)
            orden = get_or_create_orden(carrito, self.request)

            orden.update_direccion_envio(self.object)
            self.success_url = reverse_lazy('ordenes:direccion')



class ActualizarDireccion(SuccessMessageMixin, UpdateView):
    model = DireccionEnvio
    template_name = "envios/actualizar.html"
    form_class = DireccionEnvioForm
    success_url = reverse_lazy('envios:direcciones-envio')
    success_message = "%(direccion1) ha sido actualizada exitosamente..."

    
    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().usuario_id:
            return redirect('carrito:miCarrito')
        return super(ActualizarDireccion, self).dispatch(request, *args, **kwargs)



class EliminarDireccion(SuccessMessageMixin, DeleteView):
    model = DireccionEnvio
    template_name = "envios/eliminar.html"
    success_url = reverse_lazy('envios:direcciones-envio')
    success_message = 'Direccion eliminada exitosamente'

    
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().defecto:
            return redirect('envios:direcciones-envio')

        if request.user.id != self.get_object().usuario_id:
            return redirect('carrito:miCarrito')
        
        if self.get_object().tiene_ordenes():
            return redirect('envios:direcciones-envio')
        return super(EliminarDireccion, self).dispatch(request, *args, **kwargs)
    
class DireccionPrincipal(View):
    model = DireccionEnvio
    def dispatch(self, request, *args, **kwargs):
        direccion = get_object_or_404(self.model, pk=kwargs['pk'])
        if request.user.id != direccion.usuario_id:
            return redirect('carrito:miCarrito')
        
        if self.model.objects.filter(usuario=self.request.user).exists():
            direccionPrincipal = self.model.objects.filter(usuario=self.request.user).filter(defecto=True)
            direccionPrincipal.first().update_defecto(False)

        direccion.update_defecto(True)
        return redirect('envios:direcciones-envio')