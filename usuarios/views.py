from django.shortcuts import render
from usuarios.forms import FormularioLogin

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
                return redirect('login2')
    else:
        miFormulario = FormularioLogin()
    return render(request, "usuarios/login/login.html", {'form': miFormulario})
