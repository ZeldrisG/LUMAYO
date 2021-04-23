from django import forms
from libros.models import Libro

class Agregar_Libro_Form(forms.ModelForm):

    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
                    'fec_publicacion': forms.DateInput(
                        attrs={'class': 'form-control', 
                            'placeholder': 'Select a date',
                            'type': 'date'
                            }),
}