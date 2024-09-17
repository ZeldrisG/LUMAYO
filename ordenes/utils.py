from django.urls import reverse
from ordenes.models import Orden

def get_or_create_orden(carrito, request):
    orden = carrito.orden

    if orden is None:
        orden = Orden.objects.create(carrito=carrito, usuario=request.user)

    if orden:
        request.session['orden_id'] = orden.orden_id
    
    return orden

def breadcrumb(libros=True, direccion=False, pago=False, confirmacion=False):
    return [
        { 'titulo': 'Libros', 'active': libros, 'url': reverse('ordenes:orden') },
        { 'titulo': 'Direccion', 'active': direccion , 'url': reverse('orden:direccion') },
        { 'titulo': 'Pago', 'active': pago, 'url': reverse('ordenes:pago') },
        { 'titulo': 'Confirmacion', 'active': confirmacion, 'url': reverse('ordenes:confirmacion') },
        ]

def destruir_orden(request):
    request.session['orden_id'] = None