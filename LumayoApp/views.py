from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):

    return render(request, "LumayoApp/home.html")

def login(request):

    return render(request, "LumayoApp/login.html")