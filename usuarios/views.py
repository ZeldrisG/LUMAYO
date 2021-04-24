from django.shortcuts import render, redirect
from usuarios.forms import FormularioLogin, FormularioCompletarPerfil
from django.contrib.auth.views import  LoginView, LogoutView
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from usuarios.models import Clientes
from django.urls import reverse_lazy

class Login_Vista(LoginView):
    template_name = 'usuarios/login/login.html'
    authentication_form = FormularioLogin

    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('usuarios:admin-perfil')
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super(Login_Vista, self).get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesion'
        return context
    



class Admin_Perfil(TemplateView):
    model = Clientes
    template_name = 'usuarios/administrar-perfil.html'



class CompletarPerfil_Vista(UpdateView):
    model = Clientes
    form_class = FormularioCompletarPerfil
    template_name = 'usuarios/completar-perfil.html'
    success_url = reverse_lazy('usuarios:admin-perfil')

    # def get_object(self):
    #     print (self.request.user.username)
    #     return self.request.user.id
   