"""usuarios URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from libros import views

urlpatterns = [
    path('', views.admin_libro, name="admin_libro"),
    path('agregar/', views.Agregar_Libro.as_view(), name="agregar_libro"),
    path('listar/', views.Listar_Libro.as_view(), name="listar_libro"),
    path('editar/<slug:pk>/', views.Editar_Libro.as_view(), name="editar_libro"),
    path('eliminar/<slug:pk>/', views.Eliminar_Libro.as_view(), name="eliminar_libro"),




]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
