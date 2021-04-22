from django.db import models

# Create your models here.

ESTADO_lIBRO = (('Nuevo', 'Nuevo'), ('Usado', 'Usado'))
LISTA_IDIOMAS = (('Español', 'Español'), 
                 ('Ingles', 'Ingles'),
                 ('Ruso', 'Ruso'),
                 ('Japones', 'Japones'),
                 ('Coreano', 'Coreano'),
                 )


class Libro(models.Model):
    id = models.IntegerField(primary_key = True)
    issn = models.CharField(max_length=8)
    titulo = models.CharField(max_length=110)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    fec_publicacion = models.DateField(auto_now=False, auto_now_add=False)
    estado = models.CharField(max_length=9, choices=ESTADO_lIBRO, default='Nuevo')
    existencias = models.IntegerField()
    idioma = models.CharField(max_length=9, choices=LISTA_IDIOMAS, default='Nuevo')
    num_pags = models.IntegerField()
    precio = models.IntegerField()
    portada = models.ImageField(upload_to = 'libros/portadas')
 
        