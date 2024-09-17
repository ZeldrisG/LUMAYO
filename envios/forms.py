from django.forms import ModelForm
from envios.models import DireccionEnvio

class DireccionEnvioForm(ModelForm):
    class Meta:
        model = DireccionEnvio
        fields = [
            'direccion1', 'direccion2', 'ciudad', 'departamento', 'pais', 'codigo_postal', 'referencia'
        ]