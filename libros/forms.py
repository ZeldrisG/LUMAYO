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
                    
}

class GeneroForm(forms.ModelForm):
    
    class Meta:
        model = Genero
        fields = '__all__'
