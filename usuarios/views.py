from django.shortcuts import render, redirect
from usuarios.forms import FormularioLogin, FormularioCompletarPerfil
from django.contrib.auth.views import  LoginView, LogoutView
from django.views.generic.edit import UpdateView
from usuarios.models import Clientes
from django.urls import reverse_lazy

class Login_Vista(LoginView):
    template_name = 'usuarios/login/login.html'
    authentication_form = FormularioLogin

    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('admin_perfil')
        return super(Login_Vista, self).dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super(Login_Vista, self).get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesion'
        return context
    

class CompletarPerfil_Vista(UpdateView):
    model = Clientes
    form_class = FormularioCompletarPerfil
    template_name = 'usuarios/completar-perfil.html'
    success_url = reverse_lazy('admin_perfil')
    slug_url_kwarg = 'slug'

def admin_perfil(request):
    
    return render(request, "usuarios/administrar-perfil.html")
 