"""Lumayo URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from LumayoApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name="inicio"),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('crear-administrador/', views.crear_admin, name="crear-admin"),
    path('admin-libro/', include('libros.urls', namespace='admin-libro')),
    path('reserva/', include('reserva.urls', namespace='reserva')),
    path('gestionar-admin/', views.gestionar_admin, name="gestionar-admin"),
    path('eliminar-admin/', views.eliminar_admin, name="eliminar-Administrador"),
    path('carrito/', include('carrito.urls', namespace='carrito')),
    path('orden/', include('ordenes.urls', namespace='orden')),
    path('envios/', include('envios.urls', namespace='envios')),
    path('metodos_pago/', include('metodos_pago.urls', namespace='metodos_pago')),
    path('foro/', include('foro.urls', namespace='foro')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
