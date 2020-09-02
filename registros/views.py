from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Estudiante
from django.views.generic import ListView
from .models import EstudianteForm

# Create your views here.
# def index(request):
#     return HttpResponse("Hola mundo")

class EstudianteList(ListView):
    model = Estudiante


def add_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            new_estudiante = form.save()

            return HttpResponseRedirect(reverse('elist'))
    else:
        form = EstudianteForm()
    
    return render(request,'registros/estudiante_form.html',{'form':form})
