from django import forms
from libros.models import Libro, Genero


class Agregar_Libro_Form(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ('id', 'issn', 'titulo', 'autor', 'editorial', 'fec_publicacion', 'estado', 'existencias', 'idioma', 'num_pags', 'precio', 'portada')
        widgets = {
                    'portada': forms.FileInput(
                        attrs={'class': 'form-control',
                            }),

                    'issn':forms.TextInput(
                        attrs = {'class': 'form-control',
                        'placeholder': '1234-1234',
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

class GeneroForm(forms.ModelForm):
    
    class Meta:
        model = Genero
        fields = '__all__'
