from django.db import models
from Lumayo import settings
from libros.models import Libro

# Create your models here.
class Reserva(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    libros = models.ManyToManyField(Libro)
    Fecha = models.DateField(blank=True, auto_now=False, auto_now_add=False, null=True)
    valor = models.IntegerField(blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True)


