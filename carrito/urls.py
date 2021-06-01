"""carrito URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from carrito import views

app_name = 'carrito'

urlpatterns = [
    path('añadir/<slug:pk>/', views.Añadir_Carrito.as_view(), name="añadir"),
    path('listar/', views.Listar_Carrito.as_view(), name="listar-carrito"),
]