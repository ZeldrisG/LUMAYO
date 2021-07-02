"""envios URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from metodos_pago import views

app_name = 'metodos_pago'

urlpatterns = [
    path('', views.TarjetaListView.as_view(), name="tarjetas"),
    path('nueva-tarjeta', views.TarjetaCreateView.as_view(), name="nueva-tarjeta"),
    path('actualizar/<int:pk>', views.TarjetaUpdateView.as_view(), name="actualizar"),
    path('eliminar/<int:pk>', views.TarjetaDeleteView.as_view(), name="eliminar"),
    path('principal/<int:pk>', views.TarjetaPrincipal.as_view(), name="principal"),
]