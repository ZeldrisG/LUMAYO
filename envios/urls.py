"""envios URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from envios import views

app_name = 'envios'

urlpatterns = [
    path('', views.DireccionesEnvioListView.as_view(), name="direcciones-envio"),
    path('agregar/', views.AgregarDireccion.as_view(), name="agregar"),
    path('actualizar/<int:pk>', views.ActualizarDireccion.as_view(), name="actualizar"),
    path('eliminar/<int:pk>', views.EliminarDireccion.as_view(), name="eliminar"),
    path('principal/<int:pk>', views.DireccionPrincipal.as_view(), name="principal"),
]