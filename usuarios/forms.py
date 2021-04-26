from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from usuarios.models import Usuario, Perfil

class FormularioLogin(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'username or email',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        label='', 
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'password',
                'class': 'form-control'

            }
        )
    )

""" class FormularioRegistro(UserCreationForms):
    class Meta:
        model = Clientes
        fields = [] """

# class FormularioCompletarPerfil(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = '__all__'
#         #fields = ('DNI','email', 'username', 'nombres', 'apellidos', 'direccion', 'lugar_nac', 'fecha_nac', 'genero', 'foto')
#         widgets = {
#                     'fecha_nac': forms.DateInput(
#                         attrs={'class': 'form-control', 
#                             'placeholder': 'Select a date',
#                             'type': 'date'
#                             }),
#         }


class FormularioPerfil(forms.ModelForm):
    
    class Meta:
        model = Perfil
        fields = ('DNI', 'nombres', 'apellidos', 'direccion', 'lugar_nac', 'fecha_nac', 'genero', 'foto')
        widgets = {
                    'fecha_nac': forms.DateInput(
                        attrs={'class': 'form-control', 
                            'placeholder': 'Select a date',
                            'type': 'date'
                            }),
        }


class FormularioUsuario(UserCreationForm):
    email = forms.EmailField(help_text='Requerido. Agrega un email valido', max_length=60)
    class Meta:
        model = Usuario
        fields = ('email', 'username')
