import threading
from django.db import models
from django.db.models.signals import post_save


from libros.mails import Mail

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
    issn = models.CharField(max_length=9, unique=True)
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
    creado_en = models.DateTimeField(auto_now_add=True)


class Noticia(models.Model):
    libro = models.ForeignKey(Libro,on_delete=models.CASCADE)

def set_noticia(sender, instance, *args, **kwargs):
    noticia = Noticia.objects.create(libro = instance)

    hilo = threading.Thread(target=Mail.send_noticia, args=[noticia])

    hilo.start()  

post_save.connect(set_noticia, sender=Libro)






    def actualizar_existencias(self, cantidad):
        self.existencias = self.existencias + cantidad
        self.save()

    
        