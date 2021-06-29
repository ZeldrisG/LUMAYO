from django.db import models

from usuarios.models import Usuario
# Create your models here.

class DireccionEnvio(models.Model):
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    direccion1 = models.CharField(max_length=200)
    direccion2 = models.CharField(max_length=200, blank=True)
    ciudad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    referencia = models.CharField(max_length=300)
    codigo_postal = models.CharField(max_length=10)
    defecto = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.codigo_postal

    def update_defecto(self, defecto=False):
        self.defecto = defecto
        self.save()
    
    def tiene_ordenes(self):
        return self.orden_set.count() >= 1
    @property
    def direccion(self):
        return '{} - {} - {}'.format(self.ciudad, self.departamento, self.pais)