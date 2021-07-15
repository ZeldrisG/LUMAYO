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

                    'issn':forms.TextInput(
                        attrs = {'class': 'form-control',
                        'placeholder': 'ISSN',
                        'type':'text',
                        'id': 'floatingInput',

                        }),

                    'fec_publicacion':forms.DateInput(format=('%Y-%m-%d'),
                        attrs={'class': 'form-control',
                        'placeholder': 'fecha de publicacion',
                        'type':'date',
                        'id':'datefield',
                        }),
}