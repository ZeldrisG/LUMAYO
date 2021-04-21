"""usuarios URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from usuarios import views

urlpatterns = [
    path('', views.Login_Vista.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
