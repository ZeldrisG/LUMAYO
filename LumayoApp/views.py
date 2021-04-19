from django.shortcuts import render, redirect

from django.contrib import messages
#from models import Clientes
from django.contrib.auth.models import User, auth

# Create your views here.

def Home(request):
    
    return render(request, "LumayoApp/home.html")

def admin_perfil(request):
    
    return render(request, "LumayoApp/administrar-perfil.html")


def crear_administrador(request):

    return render(request, "LumayoApp/crear-administrador.html")



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('Administar Libro')
        else:
            messages.info(request, 'Credenciales incorrectas')
            return redirect('login')
    else:
        return render(request, "LumayoApp/login.html")

def admin_libro(request):
    
    return render(request, "LumayoApp/administrar-libro.html")
