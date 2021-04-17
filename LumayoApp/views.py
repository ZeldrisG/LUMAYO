from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):
    
    return render(request, "LumayoApp/home.html")


def crear_administrador(request):

    return render(request, "LumayoApp/crear-administrador.html")