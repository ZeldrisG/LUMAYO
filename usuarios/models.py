from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from Lumayo import settings


GENERO = [('M', 'Masculino'),('F', 'Femenino'), ('O', 'Otro')]
PREFERENCIAS = [('terror', 'terror'),('drama','drama'),( 'ficcion','ficcion' )]


class UsuarioManager(BaseUserManager):

    def _create_user(self, username, email, password,is_staff,is_admin, is_superuser, **extra_fields):        
        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            is_staff = is_staff,
            is_admin = is_admin,
            is_superuser = is_superuser,
            **extra_fields
            )
        usuario.set_password(password)
        usuario.save(using=self.db)
        return usuario

    def create_user(self, username, email, password, is_admin, **extra_fields):        
        return self._create_user(username, email, password, False, is_admin, False, **extra_fields)
    

    def create_superuser(self, username, email, password, **extra_fields):        
        return self._create_user(username, email, password, True, False, True, **extra_fields)
    



class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo electronico', unique=True, max_length=254)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)


    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def getTipo(self):
        return self.is_admin

    def __str__(self):
        return self.username



class Perfil(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    DNI = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50, blank=True)
    apellidos = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=50, blank=True)
    lugar_nac = models.CharField(max_length=20, blank=True)
    fecha_nac = models.DateField(auto_now=False, auto_now_add=False)
    genero=models.CharField(
        max_length=20,
        choices= GENERO,
        default= 'O'
    )


    foto = models.ImageField(upload_to = 'usuarios/fotos')

    REQUIRED_FIELDS = ['DNI','nombres']

# class Cliente(Usuario, DatosBasicos):
#     user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
#     preferencias = models.CharField(
#         max_length=20,
#         choices= PREFERENCIAS,
#         default= 'terror'
#     )

# class Admin(Usuario, DatosBasicos):
#     user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
#     preferencias = models.CharField(
#         max_length=20,
#         choices= PREFERENCIAS,
#         default= 'terror'
#     )


class Preferencia(models.Model):
    #usuario = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.CASCADE)
    preferencia=models.CharField(
        max_length=20,
        choices= PREFERENCIAS,
        default= 'terror'
    )