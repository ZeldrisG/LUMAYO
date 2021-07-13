from reserva.models import Reserva

def get_or_create_reserva(request):
    reserva = Reserva.objects.filter(usuario=request.user).first()
    if reserva is None:
        reserva = Reserva.objects.create(usuario=request.user)
    else:
        for item in reserva.libros_relacionados():
            if item.estado:
                item.update_estado()
    
    return reserva
