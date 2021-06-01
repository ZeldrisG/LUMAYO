from django import forms
from carrito.models import Carrito

class Agregar_Carrito_Form(forms.ModelForm):

    class Meta:
        model = Carrito
        fields = '__all__'