from django.shortcuts import render, redirect,HttpResponse
from usuarios.forms import FormularioLogin, FormularioPerfil, FormularioUsuario
from django.contrib.auth.views import  LoginView, LogoutView
from django.views.generic.edit import UpdateView,CreateView
from django.views.generic.base import TemplateView
from usuarios.models import Usuario, Perfil
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
    
class Modulo_Root(TemplateView):
    model = Usuario
    template_name = 'usuarios/modulo-root.html'


class Admin_Perfil(TemplateView):
    model = Usuario
    template_name = 'usuarios/administrar-perfil.html'



class CompletarPerfil_Vista(UpdateView):
    model = Usuario
    second_model = Perfil
    form_class = FormularioUsuario
    second_form_class = FormularioPerfil
    

    template_name = 'usuarios/completar-perfil.html'
    success_url = reverse_lazy('usuarios:admin-perfil')

    def get_object(self):
        print (self.request.user)
        return self.request.user

    # def get_context_data(self, **kwargs):
    #     context = super(CompletarPerfil_Vista, self).get_context_data(**kwargs)
    #     pk = self.kwargs.get('pk', 0)
    #     if 'form' not in context:
    #         context['form'] = self.form_class(self.request.GET)
    #     if 'form2' not in context:
    #         context['form2'] = self.second_form_class(self.request.GET)
    #     return context
    
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object
    #     form = self.form_class(request.POST)
    #     form2 = self.second_form_class(request.POST)

    #     if form.is_valid() and form2.is_valid():
    #         solicitud  = form2.save(commit=False)
    #         solicitud.usuario = self.model
    #         solicitud.save()
    #         return redirect(self.get_success_url())
    #     else:
    #         print ("form is invalid")
    #         print(form.errors)
    #         return self.render_to_response(self.get_context_data(form=form, form2=form2))

    def form_invalid(self, form):
        print ("form is invalid")
        print(form.errors)
        print(self.request)
        return HttpResponse("form is invalid.. this is just an HttpResponse object")



class Agregar_Admin(CreateView):
    model = Usuario
    form_class = FormularioPerfil
    template_name = 'usuarios/agregar-admin.html'
    success_url = reverse_lazy('usuarios:modulo-root')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print ("form is invalid")
        print(form.errors)
        print(self.request)
        return HttpResponse("form is invalid.. this is just an HttpResponse object")
 
   