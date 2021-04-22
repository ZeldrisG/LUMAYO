from django.shortcuts import render, redirect

from django.contrib import messages
#from models import Clientes
from django.contrib.auth.models import User, auth

# Create your views here.

def Home(request):
    
    return render(request, "LumayoApp/home.html")

def admin_perfil(request):
    
    return render(request, "LumayoApp/administrar-perfil.html")


def crear_admin(request):

    return render(request, "LumayoApp/crear-admin.html")


def gestionar_admin(request):
    
    return render(request, "LumayoApp/gestionar-admin.html")
