"""carrito URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from carrito import views

app_name = 'carrito'

urlpatterns = [
    path('editar/<slug:pk>/', views.Editar_Libro.as_view(), name="editar-libro"),
]