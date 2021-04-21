from django.shortcuts import render, redirect
from usuarios.forms import FormularioLogin
from django.contrib import auth, messages
from django.views.generic import DeleteView




def login(request):
    if request.method == 'POST':

        miFormulario = FormularioLogin(request.POST)

        if miFormulario.is_valid():
            username = miFormulario.cleaned_data['username']
            password = miFormulario.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('Administar Libro')
            else:
                messages.info(request, 'Credenciales incorrectas')
                return redirect('login')
    else:
        miFormulario = FormularioLogin()
    return render(request, "usuarios/login/login.html", {'form': miFormulario})

