"""usuarios URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from usuarios import views
app_name = 'usuarios'
urlpatterns = [
    path('', views.Loader.as_view(), name="usuarios"),
    path('admin-perfil', views.Admin_Perfil.as_view(), name="admin-perfil"),
    path('login/', views.Login_Vista.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('completar-perfil/', views.CompletarPerfil_Vista.as_view(), name="completar-perfil"),
    path('modulo-root/', views.Modulo_Root.as_view(), name="modulo-root"),
    path('agregar-admin/', views.Agregar_Admin.as_view(), name="agregar-admin"),
    path('listar-admin/', views.Listar_Admin.as_view(), name="listar-admin"),
    path('eliminar-admin/<slug:pk>/', views.Eliminar_Admin.as_view(), name="eliminar-admin"),
    path('registro/', views.Registro.as_view(), name="registro"),
    path('editar-perfil/', views.EditarPerfil.as_view(), name="editar-perfil"),
    path('modulo-admin/', views.Modulo_Admin.as_view(), name="modulo-admin"),
    path('registro-cliente/', views.Registro_Cliente.as_view(), name="registro-cliente"),
    path('completar-perfil-cliente/', views.CompletarPerfil_Vista_Cliente.as_view(), name="completar-perfil-cliente"),
    path('registro-perfil-cliente/', views.Registro_Perfil_Cliente.as_view(), name="registro-perfil-cliente"),
    path('editar-perfil-cliente/', views.EditarPerfilCliente.as_view(), name="editar-perfil-cliente"),


    


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
