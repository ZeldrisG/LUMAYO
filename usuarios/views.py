from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.views import  LoginView, LogoutView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
import time

from usuarios.models import Usuario, Perfil
from usuarios.forms import FormularioLogin, FormularioPerfil, FormularioUsuario, FormularioUsuarioAdmin
from usuarios.mixins import RootLoginMixin, AdminLoginMixin



class Login_Vista(LoginView):
    template_name = 'usuarios/login/login.html'
    authentication_form = FormularioLogin

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if self.request.user.is_superuser:
                return redirect('usuarios:modulo-root')
            elif self.request.user.is_admin:
                return redirect('usuarios:admin-perfil')                    
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(Login_Vista, self).get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesion'
        return context
    
class Modulo_Root(RootLoginMixin, TemplateView):
    model = Usuario
    template_name = 'usuarios/modulo-root.html'


class Admin_Perfil(AdminLoginMixin, TemplateView):
    model = Usuario
    template_name = 'usuarios/administrar-perfil.html'



class CompletarPerfil_Vista(AdminLoginMixin, UpdateView):
    model = Usuario
    second_model = Perfil
    form_class = FormularioUsuario
    second_form_class = FormularioPerfil

    template_name = 'usuarios/completar-perfil.html'
    success_url = reverse_lazy('usuarios:registro')
    

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
    
    def form_valid(self, form):
        solicitud = form.save(commit = False)
        form.save()
        update_session_auth_hash(self.request, self.request.user)
        return super().form_valid(form)



class EditarPerfil(AdminLoginMixin, UpdateView):
    model = Usuario
    second_model = Perfil
    form_class = FormularioUsuario
    second_form_class = FormularioPerfil

    template_name = 'usuarios/editar-perfil.html'
    success_url = reverse_lazy('usuarios:admin-perfil')
    
    def get_object(self):
        print (self.request.user)
        return self.request.user

    def get_context_data(self, **kwargs):

        context = super(EditarPerfil, self).get_context_data(**kwargs)
        #pk = self.kwargs.get('pk')
        if 'form' not in context:
            context['form'] = self.form_class(self.request.user.id)
        if 'form2' not in context:
            datos = Perfil.objects.get(usuario_id = self.request.user.id)
            context['form2'] = self.second_form_class(self.request.user)
        print (self.request.user.id)
        print (self.request.user)
        return context



class Agregar_Admin(RootLoginMixin, CreateView):
    model = Usuario
    form_class = FormularioUsuarioAdmin
    template_name = 'usuarios/agregar-admin.html'
    success_url = reverse_lazy('usuarios:modulo-root')

    def form_valid(self, form):
        user = form.save(commit = False)
        user.is_admin = True
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print ("form is invalid")
        print(form.errors)
        print(self.request)
        return HttpResponse("form is invalid.. this is just an HttpResponse object")
 

class Listar_Admin(RootLoginMixin, ListView):
    model = Usuario
    template_name = 'usuarios/listar-admin.html'
    success_url = reverse_lazy('usuarios:listar-admin')

class Eliminar_Admin(RootLoginMixin, DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar-admin.html'
    success_url = reverse_lazy('usuarios:listar-admin')




class Registro(AdminLoginMixin, CreateView):
    model=Perfil
    form_class=FormularioPerfil
    template_name='usuarios/perfil-usuario.html'
    success_url = reverse_lazy('usuarios:admin-perfil')

    def form_valid(self, form):
        print (self.request.user)
        usuario = Usuario.objects.get(username=self.request.user)
        solicitud = form.save(commit = False)
        solicitud.usuario = usuario
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print ("form is invalid")
        print(form)
        print(self.request.FILES)
        return HttpResponse("form is invalid.. this is just an HttpResponse object")


class Loader(TemplateView):
    model = Usuario
    template_name = 'usuarios/loader.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if self.request.user.is_superuser:
                return redirect('usuarios:modulo-root')
            elif self.request.user.is_admin:
                return redirect('usuarios:admin-perfil')                    
        return super().dispatch(request, *args, **kwargs)