"""usuarios URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from libros import views

urlpatterns = [
    path('', views.admin_libro, name="admin_libro"),
    path('add-libro/', views.add_libro.as_view(), name="add_libro"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
