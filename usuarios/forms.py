from django import forms
from django.contrib.auth.forms import AuthenticationForm
from usuarios.models import Clientes

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

class FormularioCompletarPerfil(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'