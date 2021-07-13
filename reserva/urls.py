"""usuarios URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from reserva import views

app_name = 'reserva'

urlpatterns = [
    path('reservar/', views.Agregar_Reserva.as_view(), name="reservar"),
    path('mis-reservas/', views.Mis_Reservas.as_view(), name="mis-reservas"),
    path('eliminar/', views.Eliminar_Reserva.as_view(), name="eliminar"),
]
