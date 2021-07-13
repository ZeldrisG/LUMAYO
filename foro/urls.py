"""envios URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from foro import views

app_name = 'foro'

urlpatterns = [
    path('', views.ForoListView.as_view(), name="foros"),
    path('crear', views.ForoCreateView.as_view(), name="crear"),
    path('foro/<int:pk>', views.ForoView.as_view(), name="foro"),
    path('comentario/editar/<int:pk>', views.ComentarioUpdateView.as_view(), name="comentario-editar"),
    path('comentario/eliminar/<int:pk>', views.ComentarioDeleteView.as_view(), name="comentario-eliminar"),
]