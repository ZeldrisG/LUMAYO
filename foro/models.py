from django.db import models

from usuarios.models import Usuario
# Create your models here.
class Foro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(blank=False, null=False, max_length=150)
    creado_en = models.DateTimeField(auto_now_add=True)
    
class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    foro = models.ForeignKey(Foro, on_delete=models.CASCADE, null=False, blank=False)
    texto = models.TextField(null=False, blank=False)
    editado_en = models.DateTimeField(auto_now_add=True)

