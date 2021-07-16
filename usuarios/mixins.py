from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin

class RootLoginMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
        return redirect('usuarios:modulo-root')

class AdminLoginMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_admin:
                return super().dispatch(request, *args, **kwargs)
        return redirect('usuarios:modulo-admin')

class ClienteLoginMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_admin and not request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
        return redirect('usuarios:login')

class RutaDeUsuarioMixin(object):
    pass
    