from django.shortcuts import render, redirect
from django.views.generic import ListView

from django.contrib import messages
#from models import Clientes
from django.contrib.auth.models import User, auth
from libros.models import Libro

# Create your views here.

class Home(ListView):
    model = Libro
    template_name = 'LumayoApp/home.html'

def crear_admin(request):

    return render(request, "LumayoApp/crear-admin.html")

def eliminar_admin(request):

    return render(request, "LumayoApp/eliminar-administrador.html")

def gestionar_admin(request):
    
    return render(request, "LumayoApp/gestionar-admin.html")
