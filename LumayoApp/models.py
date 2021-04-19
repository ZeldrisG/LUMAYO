from django.db import models

# Create your models here.

class Clientes(models.Model):
    usuario=models.CharField(max_length=20)
    contraseña=models.CharField(max_length=20)
    """ direccion=models.CharField(max_length=50)
    email=models.EmailField()
    celular=models.CharField(max_length=10) """
    nombre=models.CharField(max_length=20)
