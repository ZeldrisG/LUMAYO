from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

GENERO = [('M', 'masculino'),('F', 'femenino'), ('O', 'otro')]
PREFERENCIAS = [('terror', 'terror'),('drama','drama'),( 'ficcion','ficcion' )]


class UsuarioManager(BaseUserManager):

    def _create_user(self, username, email, password,is_staff, is_superuser, **extra_fields):        
        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
            )
        usuario.set_password(password)
        usuario.save(using=self.db)
        return usuario

    def create_user(self, username, email, password = None, **extra_fields):        
        return self._create_user(username, email, password, False, False, **extra_fields)
    

    def create_superuser(self, username, email, password = None, **extra_fields):        
        return self._create_user(username, email, password, True, True, **extra_fields)
    



class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo electronico', unique=True, max_length=254)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'Usuario {self.username}'




class DatosBasicos(models.Model):
    DNI = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    lugar_nac = models.CharField(max_length=20)
    fecha_nac = models.DateField()
    genero=models.CharField(
        max_length=20,
        choices= GENERO,
        default= 'O'
    )
    foto = models.ImageField(upload_to = 'usuarios/fotos')

    class Meta:
        abstract = True
    

class Admin(Usuario, DatosBasicos):
    def __str__(self):
        return f'Administrador {self.username}'

    

class Clientes(Usuario, DatosBasicos):
    preferencias = models.CharField(
        max_length=20,
        choices= PREFERENCIAS,
        default= 'terror'
    )
