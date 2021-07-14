from django.template.loader import get_template
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from Lumayo import settings

class Mail:

    @staticmethod
    def get_absolute_url(url):
        if settings.DEBUG:
            return 'http://localhost:8000{}'.format(
                reverse(url)
            )

    @staticmethod
    def send_admin_creado(usuario, password):
        asunto = 'Tu cuenta de administrador ha sido creada!...'
        templeate = get_template('usuarios/mails/completado.html')
        contenido = templeate.render({
            'usuario' : usuario,
            'password': password,
            'next_url': Mail.get_absolute_url('inicio')
        })


        mensaje = EmailMultiAlternatives(asunto, 'Mensaje Importante', settings.EMAIL_HOST_USER,[usuario.email])

        mensaje.attach_alternative(contenido, 'text/html')

        mensaje.send()