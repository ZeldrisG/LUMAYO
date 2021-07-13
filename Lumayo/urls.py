"""Lumayo URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

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


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="LumayoApp/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="LumayoApp/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="LumayoApp/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="LumayoApp/password_reset_done.html"), name = "password_reset_complete"),
    path('password/', auth_views.PasswordChangeView.as_view(template_name="LumayoApp/password.html"), name = "password"),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name="LumayoApp/password_change_done.html"), name = "password_change_done"),

    path('metodos_pago/', include('metodos_pago.urls', namespace='metodos_pago')),
    path('foro/', include('foro.urls', namespace='foro')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
