from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView


from compra.models import Compra, Tarjeta
from compra.forms import AgregarTarjetaForm
from libros.models import Libro
# Create your views here.

class Comprar(CreateView):
    model = Compra
    template_name = 'compra/compra.html'

    def post(self, request, *args, **kwargs):
        if request.POST.get('btnComprar') == 'Comprar':
            cantidad = request.POST.get('cantidad')
            idLibro = request.POST.get('idLibro')
            libro = Libro.objects.get(id=idLibro)
            context = {
                'object': libro,
                'cantidad' : cantidad
            }

            return render(request, self.template_name, context)
        elif request.POST.get('btnPagar') == 'Pagar':
            print(request.POST)
            return render(request, self.template_name)
        else:
            return render(request, self.template_name)


class AgregarTarjeta(CreateView):
    model = Tarjeta
    form_class = AgregarTarjetaForm
    template_name = 'compras/agregar-tarjeta.html'