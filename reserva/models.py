from django.db import models
from django.utils import timezone
from Lumayo import settings
from libros.models import Libro

# Create your models here.
class Reserva(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    libros = models.ManyToManyField(Libro, through = 'ReservaLibros')

class ReservaLibros(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete = models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete = models.CASCADE)
    fec_reserva = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField(null = True)

