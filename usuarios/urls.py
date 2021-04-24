"""usuarios URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from usuarios import views
app_name = 'usuarios'
urlpatterns = [
    path('', views.Admin_Perfil.as_view(), name="admin-perfil"),
    path('login/', views.Login_Vista.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('completar-perfil/<int:pk>', views.CompletarPerfil_Vista.as_view(), name="completar-perfil"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
