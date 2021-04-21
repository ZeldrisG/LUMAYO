from django import forms
from django.contrib.auth.forms import AuthenticationForm

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