from django import forms
from foro.models import Foro, Comentario

class ForoForm(forms.ModelForm):

    class Meta:
        model = Foro
        fields = ['titulo']

class ComentarioForm(forms.ModelForm):
    
    class Meta:
        model = Comentario
        fields = ['texto']