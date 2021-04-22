"""Lumayo URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from LumayoApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.Home, name="inicio"),
    path('admin-perfil/', views.admin_perfil, name="admin_perfil"),
    path('crear-administrador/', views.crear_admin, name="crear_admin"),
    path('login/', include('usuarios.urls'), name="login"),
    path('admin-libro/', include('libros.urls'), name="admin_libro"),
    path('add-libro/', include('libros.urls'), name="add_libro"),
    path('gestionar-admin/', views.gestionar_admin, name="Gestionar_admin"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
