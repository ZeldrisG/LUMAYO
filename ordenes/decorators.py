from ordenes.utils import get_or_create_orden
from carrito.utils import get_create_carrito

def validar_carrito_y_orden(fuction):
    def wrap(request, *args, **kwargs):
        carrito = get_create_carrito(request)
        orden = get_or_create_orden(carrito, request)
        return fuction(request, carrito, orden, *args, **kwargs)

    return wrap