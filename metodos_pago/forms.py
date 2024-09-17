from django import forms
from django.forms import ModelForm
from metodos_pago.models import Tarjeta, TipoTarjeta

class TarjetaForm(ModelForm):
    
    class Meta:
        model = Tarjeta
        fields = [
            'nombre_apellido', 'numero', 'fec_expiracion', 'cvc', 'saldo'
        ]