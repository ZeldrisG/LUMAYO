from django.shortcuts import render, redirect
from django.contrib.auth.views import  LoginView, LogoutView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
import time

from usuarios.models import Preferencia, Usuario, Perfil
from usuarios.forms import FormularioLogin, FormularioPerfil, FormularioUsuario, FormularioUsuarioAdmin, FormularioUsuarioCliente, FormularioPreferencias, FormularioEditarPerfil
from usuarios.mixins import RootLoginMixin, AdminLoginMixin
from reserva.models import Reserva



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


class Admin_Perfil(TemplateView):
    model = Usuario
    template_name = 'usuarios/administrar-perfil.html'


class Modulo_Admin(AdminLoginMixin, TemplateView):
    model = Usuario
    template_name = 'usuarios/modulo-admin.html'




class CompletarPerfil_Vista(AdminLoginMixin, UpdateView):
    model = Usuario
    form_class = FormularioUsuario

    template_name = 'usuarios/completar-perfil.html'
    success_url = reverse_lazy('usuarios:registro')

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Registro(AdminLoginMixin, CreateView):
    model=Perfil
    form_class=FormularioPerfil
    template_name='usuarios/perfil-usuario.html'
    success_url = reverse_lazy('usuarios:admin-perfil')

    def form_valid(self, form):
        print (self.request.user)
        usuario = Usuario.objects.get(username=self.request.user)
        form = self.form_class(self.request.POST, self.request.FILES)
        solicitud = form.save(commit = False)
        solicitud.usuario = usuario
        form.save()
        return super().form_valid(form)

class EditarPerfil(AdminLoginMixin, UpdateView):
    model = Usuario
    second_model = Perfil
    form_class = FormularioUsuario
    second_form_class = FormularioEditarPerfil

    template_name = 'usuarios/editar-perfil.html'
    success_url = reverse_lazy('usuarios:admin-perfil')
    
    def get_object(self):
        print (self.request.user)
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(EditarPerfil, self).get_context_data(**kwargs)
        datos = Perfil.objects.get(usuario_id = self.request.user.id)
        formulario = FormularioPerfil(instance=datos)
        context['form2'] = formulario
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        usuario = self.model.objects.get(id=request.user.id)
        perfil = Perfil.objects.get(usuario_id=request.user.id)
        form = self.form_class(request.POST, instance = usuario)
        form2 = self.second_form_class(request.POST, request.FILES, instance= perfil)

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect(self.get_success_url())
        else:
            print(form.errors)
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


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


class Listar_Admin(RootLoginMixin, ListView):
    model = Usuario
    template_name = 'usuarios/listar-admin.html'
    success_url = reverse_lazy('usuarios:listar-admin')
    queryset = model.objects.filter(is_admin=True)
    ordering = ["id"]

class Eliminar_Admin(RootLoginMixin, DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar-admin.html'
    success_url = reverse_lazy('usuarios:listar-admin')


class Loader(TemplateView):
    model = Usuario
    template_name = 'usuarios/loader.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if self.request.user.is_superuser:
                return redirect('usuarios:modulo-root')
            elif self.request.user.is_admin:
                return redirect('usuarios:modulo-admin')
            elif not self.request.user.is_admin:
                return redirect('inicio')
        return super().dispatch(request, *args, **kwargs)


class Registro_Cliente(CreateView):
    model = Usuario
    form_class = FormularioUsuarioAdmin
    template_name = 'usuarios/registro-cliente.html'
    success_url = reverse_lazy('usuarios:login')

    def form_valid(self, form):
        user = form.save(commit = False)
        user.is_admin = False
        user.save()
        return super().form_valid(form)


# Completar, editar perfil cliente
class CompletarPerfil_Vista_Cliente(UpdateView):
    model = Usuario
    form_class = FormularioUsuario

    template_name = 'usuarios/completar-perfil.html'
    success_url = reverse_lazy('usuarios:registro-perfil-cliente')

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Registro_Perfil_Cliente(CreateView):
    model=Perfil
    second_model = Preferencia
    form_class=FormularioPerfil
    second_form_class = FormularioPreferencias

    template_name='usuarios/perfil-usuario.html'
    success_url = reverse_lazy('usuarios:admin-perfil')

    def get_object(self):
        #print (self.request.user)
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(Registro_Perfil_Cliente, self).get_context_data(**kwargs)
        
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            usuario = Usuario.objects.get(username=self.request.user)
            solicitud = form.save(commit = False)
            solicitud.usuario = usuario
            solicitud2 = form2.save(commit = False)
            solicitud2.perfil = form.save()
            solicitud2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            print ("form is invalid")
            print(form.errors)
            return self.render_to_response(self.get_context_data(form=form, form2=form2))
    
class EditarPerfilCliente(UpdateView):
    model = Usuario
    second_model = Perfil
    third_model = Preferencia
    form_class = FormularioUsuario
    second_form_class = FormularioEditarPerfil
    third_form_class = FormularioPreferencias

    template_name = 'usuarios/editar-perfil-cliente.html'
    success_url = reverse_lazy('usuarios:admin-perfil')
    
    def get_context_data(self, **kwargs):
        context = super(EditarPerfilCliente, self).get_context_data(**kwargs)
        datos = Perfil.objects.get(usuario_id = self.request.user.id)
        datos2 = Preferencia.objects.get(perfil = datos.DNI)
        formulario = FormularioPerfil(instance=datos)
        formulario2 = FormularioPreferencias(instance=datos2)
        context['form2'] = formulario
        context['form3'] = formulario2
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        usuario = self.model.objects.get(id=request.user.id)
        perfil = Perfil.objects.get(usuario_id=request.user.id)
        preferencia = Preferencia.objects.get(perfil=perfil.DNI)
        form = self.form_class(request.POST, instance = usuario)
        form2 = self.second_form_class(request.POST, request.FILES, instance= perfil)
        form3 = self.third_form_class(request.POST, instance= preferencia)
        print ("Form 1", form)
        print ("Form 2", form2)
        print ("Form 3", form3)


        if form.is_valid() and form2.is_valid() and form3.is_valid():
            form.save()
            form2.save()
            form3.save()
            return redirect(self.get_success_url())
        else:
            print ("form is invalid")
            print(form.errors)
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))