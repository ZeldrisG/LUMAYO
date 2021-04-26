"""Lumayo URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from LumayoApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.Home, name="inicio"),
    path('admin-perfil/', include('usuarios.urls', namespace='admin-perfil')),
    path('crear-administrador/', views.crear_admin, name="crear-admin"),
    path('admin-libro/', include('libros.urls', namespace='admin-libro')),
    path('gestionar-admin/', views.gestionar_admin, name="gestionar-admin"),
    path('eliminar-admin/', views.eliminar_admin, name="eliminar-Administrador"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
