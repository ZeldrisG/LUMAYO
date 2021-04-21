from django.db import models
from django.contrib.auth.models import User

class Clientes(User):
    genero=models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    lugar_nac = models.CharField(max_length=20)
