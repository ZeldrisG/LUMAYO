from django.db import models
from django.db.models.signals import pre_save, m2m_changed, post_save
import uuid
from Lumayo import settings
from libros.models import Libro
from ordenes.common import OrdenEstado

class CarritoCompras(models.Model):
    carritocompras_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    libros = models.ManyToManyField(Libro, through='CarritoLibros')
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    creado_en = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'soy un carrito'
    
    def update_totals(self):
        self.update_subtotal()
        self.update_total()

        if self.orden:
            self.orden.update_total()

    def update_subtotal(self):
        self.subtotal = sum([
            item.cantidad * item.libro.precio for item in self.libros_relacionados()
         ])
        self.save()
    
    def update_total(self):
        self.total = sum([
            item.cantidad * item.libro.precio for item in self.libros_relacionados()
         ])
        self.save()

    def libros_relacionados(self):
        return self.carritolibros_set.select_related('libro')

    @property
    def orden(self):
        return self.orden_set.filter(estado=OrdenEstado.CREADO).first()


class CarritoLibrosManager(models.Manager):
    def create_or_update_cantidad(self, carrito, libro, cantidad=1):
        objecto, creado = self.get_or_create(carrito=carrito, libro=libro)

        if not creado:
            cantidad = objecto.cantidad + cantidad
        
        objecto.update_cantidad(cantidad)
        return objecto


class CarritoLibros(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    creado_en = models.DateTimeField(auto_now_add=True)

    objects = CarritoLibrosManager()

    def update_cantidad(self, cantidad=1):
        self.cantidad = cantidad
        self.save()

def set_carrito_id(sender, instance, *args, **kwargs):
    if not instance.carritocompras_id:
        instance.carritocompras_id = str(uuid.uuid4())

def update_totals(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()


def post_save_update_totals(sender, instance, *args, **kwargs):
    instance.carrito.update_totals()

pre_save.connect(set_carrito_id, sender=CarritoCompras)
post_save.connect(post_save_update_totals, sender=CarritoLibros)
m2m_changed.connect(update_totals, sender=CarritoCompras.libros.through)