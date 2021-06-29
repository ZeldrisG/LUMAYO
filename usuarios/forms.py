from django import forms
from django.contrib.auth import (authenticate)
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from datetime import date

from usuarios.models import Usuario, Perfil, Preferencia

class FormularioLogin(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'Nombre de usuario',
            }
        )
    )

    password = forms.CharField(
        label='', 
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña',
            }
        )
    )

    # def clean(self, *args, **kwargs):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')

    #     if username and password:
    #         print(username, password)
    #         self.user_cache = authenticate(self.request, username=username, password=password)
    #         if not self.user_cache:
    #             raise forms.ValidationError('Este usuario no existe!...')
    #         if not self.user_cache.check_password(password):
    #             raise forms.ValidationError('Contraseña incorrecta!...')
    #         if not self.user_cache.is_active:
    #             raise forms.ValidationError('Este usuario no esta activo!...')
        
    #     return super(FormularioLogin, self).clean(*args, kwards)



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
                    'foto': forms.FileInput(
                        attrs={'class': 'form-control',
                            }),
        }
    
class FormularioEditarPerfil(forms.ModelForm):
    
    class Meta:
        model = Perfil
        fields = ('DNI', 'nombres', 'apellidos', 'direccion', 'lugar_nac', 'fecha_nac', 'genero', 'foto')
        widgets = {
                    'foto': forms.FileInput(
                        attrs={'class': 'form-control',
                            }),
        }


class FormularioUsuario(forms.ModelForm):
    email = forms.EmailField(help_text='Requerido. Agrega un email valido', max_length=60)
    class Meta:
        model = Usuario
        fields = ('email', 'username')


class FormularioUsuarioAdmin(UserCreationForm):
    email = forms.EmailField(help_text='Requerido. Agrega un email valido', max_length=60)    
    class Meta:
        model = Usuario
        fields = ('username', 'email',)
        widgets = {
                    'password': forms.PasswordInput(
                        attrs={'class': 'form-control', 
                            'placeholder': 'Contraseña',
                            }),   
        }

class FormularioUsuarioCliente(UserCreationForm):
    email = forms.EmailField(help_text='Requerido. Agrega un email valido', max_length=60)    
    class Meta:
        model = Usuario
        fields = ('username', 'email',)
        widgets = {
                    'password': forms.PasswordInput(
                        attrs={'class': 'form-control', 
                            'placeholder': 'Contraseña',
                            }),   
        }


class FormularioPreferencias(forms.ModelForm):
    class Meta:
        model = Preferencia
        fields = ('preferencia',)