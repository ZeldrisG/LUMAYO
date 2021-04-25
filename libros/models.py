from django.db import models

# Create your models here.

ESTADO_lIBRO = (('Nuevo', 'Nuevo'), ('Usado', 'Usado'))
LISTA_IDIOMAS = (('Español', 'Español'), 
                 ('Ingles', 'Ingles'),
                 ('Ruso', 'Ruso'),
                 ('Japones', 'Japones'),
                 ('Coreano', 'Coreano'),
                 )

# class Genero(models.Model):
#     nombre = models.CharField(max_length=50)
#     libro = models.ManyToManyField(Libro)

#     def __str__(self):
#         return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    issn = models.CharField(max_length=8)
    titulo = models.CharField(max_length=110)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    fec_publicacion = models.DateField(auto_now=False, auto_now_add=False)
    estado = models.CharField(max_length=50, choices=ESTADO_lIBRO, default='Nuevo')
    existencias = models.IntegerField()
    idioma = models.CharField(max_length=50, choices=LISTA_IDIOMAS, default='Español')
    num_pags = models.IntegerField()
    precio = models.IntegerField()
    portada = models.ImageField(upload_to = 'libros/portadas')

    
        