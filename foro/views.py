from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

from foro.models import Foro, Comentario
from foro.forms import ForoForm, ComentarioForm
# Create your views here.


class ForoListView(ListView):
    model = Foro
    template_name = "foro/foros.html"


class ForoCreateView(SuccessMessageMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = "foro/crear.html"
    success_url = reverse_lazy('foro:foros')
    success_message = "El foro ha sido creado exitosamente..."

    
    def get_context_data(self, **kwargs):
        context = super(ForoCreateView, self).get_context_data(**kwargs)
        foroForm = ForoForm()
        context['foroForm'] = foroForm
        return context
    

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        titulo = self.request.POST.get('titulo')
        print(titulo)
        foro = Foro.objects.create(usuario=self.request.user, titulo=titulo)
        self.object.foro = foro
        self.object.save()
        return super().form_valid(form)


class ForoView(View):
    model = Foro
    template_name = "foro/foro.html"
    object = None
    
    def get(self, request, *args, **kwargs):
        foro = get_object_or_404(self.model, pk=kwargs['pk'])
        comentarios = Comentario.objects.filter(foro=foro)
        self.context = {
            'foro' : foro,
            'comentarios' : comentarios
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        foro = get_object_or_404(self.model, pk=kwargs['pk'])
        texto = self.request.POST.get('comentario')
        comentario = Comentario.objects.create(usuario=request.user, texto=texto, foro=foro)
        return redirect('foro:foro',kwargs['pk'])


class ComentarioUpdateView(UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = "foro/actualizar.html"
    
    def get_success_url(self):
        print(self.object.foro.pk)
        return reverse_lazy('foro:foro', kwargs={'pk': self.object.foro.pk})


class ComentarioDeleteView(DeleteView):
    model = Comentario
    template_name = "foro/eliminar.html"
    
    def get_success_url(self):
        print(self.object.foro.pk)
        return reverse_lazy('foro:foro', kwargs={'pk': self.object.foro.pk})
