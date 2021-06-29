from django.urls import path

from perfiles_facturacion import views

app_name = 'perfiles_facturacion'

urlpatterns = [
    path('nuevo/', views.PerfilFacturacionCreateView.as_view(), name='nuevo'), 
      
]