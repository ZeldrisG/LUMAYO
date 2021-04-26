
class AdminUsuarioMixin(object):

    
    def dispatch(self, request, *args, **kwargs):
        if reques.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
    return redirect('inicio')
    