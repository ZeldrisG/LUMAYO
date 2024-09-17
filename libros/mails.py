from django.template.loader import get_template
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from Lumayo import settings

from usuarios.models import Usuario
class Mail:

    @staticmethod
    def get_absolute_url(url):
        if settings.DEBUG:
            return 'http://localhost:8000{}'.format(
                reverse(url)
            )

    @staticmethod
    def send_noticia(noticia):
        asunto = 'Nuevo libro disponible, ¡Podria interesarte!'
        templeate = get_template('libros/mails/noticia.html')
        usuarios = Usuario.objects.filter(is_admin = False).filter(is_superuser = False)

        for usuario in usuarios:

            contenido = templeate.render({
                'usuario' : usuario,
                'noticia' : noticia,
                'next_url': Mail.get_absolute_url('inicio')
            })


            mensaje = EmailMultiAlternatives(asunto, 'Mensaje Importante', settings.EMAIL_HOST_USER,[usuario.email])

            mensaje.attach_alternative(contenido, 'text/html')

            mensaje.send()