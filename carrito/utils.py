from carrito.models import CarritoCompras as Carrito

def get_create_carrito(request):
    usuario = request.user if request.user.is_authenticated else None
    carrito_id = request.session.get('carritocompras_id')
    carrito = Carrito.objects.filter(carritocompras_id=carrito_id).first()
    if carrito is None:
        carrito = Carrito.objects.create(usuario=usuario)
    
    if usuario and carrito.usuario is None:
        carrito.usuario = usuario
        carrito.save()

    request.session['carritocompras_id'] = carrito.carritocompras_id

    return carrito

def destruir_carrito(request):
    request.session['carritocompras_id'] = None