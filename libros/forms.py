from django import forms
from libros.models import Libro

class Agregar_Libro_Form(forms.ModelForm):

    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {

                    
                    'portada': forms.FileInput(
                        attrs={'class': 'form-control',
                            }),
}