"""carrito URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from carrito import views

app_name = 'carrito'

urlpatterns = [
    path('miCarrito/', views.CarritoView.as_view(), name="miCarrito"),
    path('agregar/', views.Agregar_Carrito.as_view(), name="agregar"),
    path('eliminar/', views.EliminarLibro_Carrito.as_view(), name="eliminar"),
]