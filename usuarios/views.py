from django.shortcuts import render, redirect
from usuarios.forms import FormularioLogin
from django.contrib.auth.views import  LoginView, LogoutView

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
    
    