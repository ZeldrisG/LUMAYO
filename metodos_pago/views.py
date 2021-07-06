from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from metodos_pago.models import Tarjeta
from metodos_pago.forms import TarjetaForm
# Create your views here.

class TarjetaListView(ListView):
    model = Tarjeta
    template_name = 'metodos_pago/tarjetas.html'

    def get_queryset(self):
        return self.model.objects.filter(usuario=self.request.user).order_by('-defecto')
    

class TarjetaCreateView(SuccessMessageMixin, CreateView):
    model = Tarjeta
    form_class = TarjetaForm
    template_name = 'metodos_pago/nueva-tarjeta.html'
    success_url = reverse_lazy('metodos_pago:tarjetas')
    success_message = "%(tipo) ha sido creada exitosamente..."

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        print('fecha')
        #cp = form.save(commit=False)
        print(form['fec_expiracion'].data)
        #print(cp)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.defecto = not self.model.objects.filter(usuario=self.request.user).exists()
        self.object.save()
        if self.request.GET.get('next'):
            self.next()
        return super().form_valid(form)
        

class TarjetaUpdateView(SuccessMessageMixin, UpdateView):
    model = Tarjeta
    template_name = "metodos_pago/actualizar.html"
    form_class = TarjetaForm
    success_url = reverse_lazy('metodos_pago:tarjetas')
    success_message = "%(numero) ha sido actualizada exitosamente..."

    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().usuario_id:
            return redirect('inicio')
        return super(TarjetaUpdateView, self).dispatch(request, *args, **kwargs)



class TarjetaDeleteView(DeleteView):
    model = Tarjeta
    template_name = "metodos_pago/eliminar.html"
    success_url = reverse_lazy('metodos_pago:tarjetas')
    success_message = 'Tarjeta eliminada exitosamente'

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().defecto:
            return redirect('metodos_pago:tarjetas')

        if request.user.id != self.get_object().usuario_id:
            return redirect('inicio')

        return super(TarjetaDeleteView, self).dispatch(request, *args, **kwargs)


class TarjetaPrincipal(View):
    model = Tarjeta
    def dispatch(self, request, *args, **kwargs):
        tarjeta = get_object_or_404(self.model, pk=kwargs['pk'])
        if request.user.id != tarjeta.usuario_id:
            return redirect('metodos_pago:tarjetas')
        
        if self.model.objects.filter(usuario=self.request.user).exists():
            tarjetaPrincipal = self.model.objects.filter(usuario=self.request.user).filter(defecto=True)
            tarjetaPrincipal.first().update_defecto(False)

        tarjeta.update_defecto(True)
        return redirect('metodos_pago:tarjetas')