from django.db import models
from Lumayo import settings
from libros.models import Libro



class Carrito(models.Model):
    fecha = models.DateField(auto_now=False, auto_now_add=False, null=True)
    valor = models.IntegerField(null=True)
    estado = models.BooleanField(null=True)
    libros = models.ManyToManyField(Libro, null=True)
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


