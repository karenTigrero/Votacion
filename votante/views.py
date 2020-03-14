from __future__ import unicode_literals 
from .models import Votante
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import VotanteForm
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.

class Inicio(TemplateView):
    template_name = 'index.html'


class ListadoVotante(ListView):
    model = Votante
    template_name = 'listadov.html'
    context_object_name = 'votantes'
    queryset = Votante.objects.filter(estado = True)

class ActualizarVotante(UpdateView):
    model = Votante
    form_class = VotanteForm
    template_name = 'editarv.html'
    success_url = reverse_lazy('listadov')

class CrearVotante(CreateView):
    model = Votante
    form_class = VotanteForm
    template_name = 'crearv.html'
    success_url = reverse_lazy('votante:listadov')

class EliminarVotante(DeleteView):
    model = Votante

    def post(self,request,pk,*args,**kwargs):
        object = Votante.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('listadov')

def voto(request, id):
    votante = Votante.objects.get(id=id)
    context = {
        'votante' : votante
    }
    return render(request, 'voto.html', context)
