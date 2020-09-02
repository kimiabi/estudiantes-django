from django.db import models
from django.forms import ModelForm

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=24)
    apellido = models.CharField(max_length=24)
    carne = models.IntegerField()

    def __unicode__(self):
        return self.carne

    def __str__(self):
        return self.nombre

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'