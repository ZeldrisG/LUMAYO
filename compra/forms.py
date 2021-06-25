from django import forms
from compra.models import CompraLibros, Tarjeta

class Compra_Form(forms.ModelForm):

    class Meta:
        model = CompraLibros
        fields = ['libro', 'cantidad']

class AgregarTarjetaForm(forms.ModelForm):
    
    class Meta:
        model = Tarjeta
        fields = ['tipo', 'numero', 'fecha_caducidad', 'cvc', 'saldo']