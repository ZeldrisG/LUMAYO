from django.db import models
from django.contrib.auth.models import User

GENERO = [('M', 'masculino'),('F', 'femenino'), ('O', 'otro')]
PREFERENCIAS = [('terror', 'terror'),('drama','drama'),( 'ficcion','ficcion' )]

class Clientes(User):
    genero=models.CharField(
        max_length=20,
        choices= GENERO,
        default= 'O'
    )
    direccion = models.CharField(max_length=50)
    lugar_nac = models.CharField(max_length=20)
    fecha_nac = models.DateField()
    foto = models.ImageField(upload_to = 'usuarios/fotos')
    DNI = models.IntegerField()
    preferencias = models.CharField(
        max_length=20,
        choices= PREFERENCIAS,
        default= 'terror'
    )
