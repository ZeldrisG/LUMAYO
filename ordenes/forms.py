from django import forms

MOTIVOS =(
    ("1", "Producto en mal estado."),
    ("2", "No cumple las expectativas."),
    ("3", "Llego en un tiempo superior a lo estipulado."),
)

class DevolucionesForm(forms.Form):
    libro = forms.CharField(max_length=100)
    motivos = forms.ChoiceField(choices = MOTIVOS)
    comentario = forms.CharField(widget=forms.Textarea)