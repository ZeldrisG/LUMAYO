"""ordenes URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from ordenes import views

app_name = 'ordenes'

urlpatterns = [
    path('', views.OrdenView.as_view(), name="orden"),
    path('direccion', views.Direccion.as_view(), name="direccion"),
    path('seleccionar/direccion', views.SeleccionarDireccion.as_view(), name="seleccionar_direccion"),
    path('establecer/direccion/<int:pk>', views.EstablecerDireccion.as_view(), name="establecer_direccion"),
    path('pago/', views.Metodo_Pago.as_view(), name="pago"),
    path('seleccionar/metodo_pago', views.SeleccionarTarjeta.as_view(), name="seleccionar_metodo_pago"),
    path('establecer/metodo_pago/<int:pk>', views.EstablecerTarjeta.as_view(), name="establecer_metodo_pago"),
    path('confirmacion/', views.Confirmacion.as_view(), name="confirmacion"),
    path('cancelar/', views.Cancelar.as_view(), name="cancelar"),
    path('completar/', views.Completar.as_view(), name="completar"),
    path('completados/', views.OrdenesListView.as_view(), name="completados"),
    path('devoluciones/', views.Devoluciones.as_view(), name="devoluciones"),

]