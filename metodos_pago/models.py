from enum import Enum
from django.db import models

# Create your models here.
from usuarios.models import Usuario

class TipoTarjeta(Enum):
    DEBITO = 'DEBITO'
    CREDITO = 'CREDITO'

opciones = [ (tag, tag.value) for tag in TipoTarjeta ]

class Tarjeta(models.Model):
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    numero = models.CharField(max_length=19, null=False, blank=False)
    nombre_apellido = models.CharField(max_length=200, null=False, blank=False)
    fec_expiracion = models.CharField(max_length=5, null=False, blank=False)
    cvc = models.CharField(max_length=3, null=False, blank=False)
    defecto = models.BooleanField(default=False, null=False, blank=False)
    creado_en = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=20, choices=opciones, default=TipoTarjeta.CREDITO)
    saldo = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.tipo[12:]
        
    def update_defecto(self, defecto=False):
        self.defecto = defecto
        self.save()
    
    def tiene_saldo(self):
        return self.saldo >= 1

    def actualizar_saldo(self, cantidad):
        self.saldo = self.saldo + cantidad
        self.save()

    def ultimos_cuatro(self):
        return self.numero[:4]
    # @property
    # def direccion(self):
    #     return '{} - {} - {}'.format(self.ciudad, self.departamento, self.pais)