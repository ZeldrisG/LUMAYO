from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):
    
    return render(request, "LumayoApp/home.html")

def admin_perfil(request):
    
    return render(request, "LumayoApp/administrar-perfil.html")


def crear_administrador(request):

    return render(request, "LumayoApp/crear-administrador.html")



def login(request):

    return render(request, "LumayoApp/login.html")

def admin_libro(request):
    
    return render(request, "LumayoApp/administrar-libro.html")
