from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):

    return render(request, "LumayoApp/home.html")

def admin_perfil(request):
    
    return render(request, "LumayoApp/administrar-perfil.html")