from datetime import timedelta
import pytz

import django
from django.db import models
from django.utils import timezone
from Lumayo import settings
from libros.models import Libro

# Create your models here.
def get_fec_reserva():
    return timezone.localtime(timezone.now())
def get_fec_expiracion():
    return timezone.localtime(timezone.now()) + timedelta(hours=24)

class Reserva(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    libros = models.ManyToManyField(Libro, through = 'ReservaLibros')

    def libros_relacionados(self):
        return self.reservalibros_set.select_related('libro')

class ReservaLibros(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete = models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete = models.CASCADE)
    fec_reserva = models.DateTimeField(default=django.utils.timezone.now)
    fec_expiracion = models.DateTimeField(default=get_fec_expiracion())
    estado = models.BooleanField(default=True, null=False, blank=False)
    cantidad = models.IntegerField(default=1 ,null = False, blank=False)
    
    class Meta:
            ordering = ["-fec_reserva"]

    def update_estado(self):
        self.estado = timezone.localtime(timezone.now()) < self.fec_expiracion
        self.save()




