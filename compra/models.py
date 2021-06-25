from django.db import models
from usuarios.models import Usuario
from Lumayo import settings
from libros.models import Libro

# Create your models here.

TIPO = [('C', 'Credito'),('D', 'Debito')]

class Compra(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    libros = models.ManyToManyField(Libro, through = 'CompraLibros')

class CompraLibros(models.Model):
    compra = models.ForeignKey(Compra, on_delete = models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete = models.CASCADE)
    fec_compra = models.DateTimeField(auto_now_add =True)
    cantidad = models.IntegerField(null = True)
    estado = models.BooleanField(blank = True)
    servicio_envio = models.CharField(blank=True, max_length=50)
    metodo_pago = models.CharField(blank=True, max_length=50)

    @property
    def valor(self):
        return self.libro.precio * self.cantidad
            

class Tarjeta(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    tipo=models.CharField(
        max_length=20,
        choices= TIPO,
        default= 'C'
    )
    numero = models.IntegerField()
    fecha_caducidad = models.DateTimeField(blank=True, auto_now=False, auto_now_add=False)
    cvc = models.IntegerField()
    saldo = models.IntegerField()