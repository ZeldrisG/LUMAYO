from django.shortcuts import redirect

class RootLoginMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
        return redirect('inicio')

class AdminLoginMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_admin:
                return super().dispatch(request, *args, **kwargs)
        return redirect('inicio')

class ClienteLoginMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_admin:
                return super().dispatch(request, *args, **kwargs)
        return redirect('inicio')

class RutaDeUsuarioMixin(object):
    pass
    