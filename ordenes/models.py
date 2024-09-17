import uuid

from django.db import models
from django.db.models.signals import pre_save

from ordenes.common import OrdenEstado, opciones
from carrito.models import CarritoCompras
from usuarios.models import Usuario
from envios.models import DireccionEnvio
from metodos_pago.models import Tarjeta

# Create your models here.



class Orden(models.Model):
    orden_id = models.CharField(unique=True, max_length=100, null=False, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=opciones, default=OrdenEstado.CREADO)

    total_envio = models.DecimalField(default=5, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)
    direccion_envio = models.ForeignKey(DireccionEnvio, on_delete=models.CASCADE, null=True, blank=True)
    metodo_pago = models.ForeignKey(Tarjeta, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.orden_id

    def get_total(self):
        return self.carrito.total + self.total_envio
    
    def update_total(self):
        self.total = self.get_total()
        self.save()

    def get_or_set_direccion_envio(self):
        if self.direccion_envio:
            return self.direccion_envio
        
        direccion_envio = DireccionEnvio.objects.filter(usuario=self.usuario).exists()
        direccionPrincipal = None
        if direccion_envio:
            direccionPrincipal = DireccionEnvio.objects.filter(usuario=self.usuario).filter(defecto=True).first()
            self.update_direccion_envio(direccionPrincipal)
        
        return direccionPrincipal
    
    def update_direccion_envio(self, direccion):
        self.direccion_envio = direccion
        self.save()

    def cancelar(self):
        self.estado = OrdenEstado.CANCELADO
        self.save()

    def completar(self):
        self.estado = OrdenEstado.COMPLETADO
        self.save()

    def get_or_set_metodo_pago(self):
        if self.metodo_pago:
            return self.metodo_pago
        
        metodo_pago = Tarjeta.objects.filter(usuario=self.usuario).exists()
        tarjetaPrincipal = None
        if metodo_pago:
            tarjetaPrincipal = Tarjeta.objects.filter(usuario=self.usuario).filter(defecto=True).first()
            self.update_metodo_pago(tarjetaPrincipal)
        
        return tarjetaPrincipal

    def update_metodo_pago(self, metodo_pago):
        self.metodo_pago = metodo_pago
        self.save()


def set_orden_id(sender, instance, *args, **kwargs):
    if not instance.orden_id:
        instance.orden_id = str(uuid.uuid4())

def set_total(sender, instance, *args, **kwargs):
    instance.total = instance.get_total()

pre_save.connect(set_orden_id, sender=Orden)
pre_save.connect(set_total, sender=Orden)