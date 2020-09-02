from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.EstudianteList.as_view(),name='elist'),
    path('add/',views.add_estudiante,name='eadd')
]

