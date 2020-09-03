from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Estudiante
from django.views.generic import ListView
from .models import EstudianteForm

# Create your views here.
class EstudianteList(ListView):
    model = Estudiante


def add_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            new_estudiante = form.save(commit=False)

            total_carne = 0
            for i in str(new_estudiante.carne):
                total_carne = total_carne + int(i)

            new_estudiante.resultado = new_estudiante.nombre[0]+' '+new_estudiante.apellido[0]+' '+str(total_carne)
            new_estudiante.save()

            return HttpResponseRedirect(reverse('elist'))
    else:
        form = EstudianteForm()
    
    return render(request,'registros/estudiante_form.html',{'form':form})
