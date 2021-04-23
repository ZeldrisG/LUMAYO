from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from libros.models import Libro
from libros.forms import AddLibroForm

# Create your views here.

def admin_libro(request):
    
    return render(request, "libros/administrar-libro.html")


class Add_Libro(CreateView):
    model = Libro
    form_class = AddLibroForm
    template_name = 'libros/agregar-libro.html'
    success_url = reverse_lazy('admin_libro')

    def form_valid(self, form):
        print ('happening2')
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print ("form is invalid")
        print(self.request.FILES)
        return HttpResponse("form is invalid.. this is just an HttpResponse object")
 


class LibroList(ListView):
    model = Libro
    template_name = 'libros/listar-libro.html'


class LibroUpdate(UpdateView):
    model = Libro
    form_class = AddLibroForm
    template_name = 'libros/actualizar-libro.html'
    success_url = reverse_lazy('admin_libro')

    def form_valid(self, form):
        print ('happening2')
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print ("form is invalid")
        print(self.request.FILES)
        return HttpResponse("form is invalid.. this is just an HttpResponse object")


class LibroDelete(DeleteView):
    model = Libro
    template_name = 'libros/eliminar-libro.html'
    success_url = reverse_lazy('list_libro')
