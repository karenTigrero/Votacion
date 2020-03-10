from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from .forms import CandidatoForm, ListaForm
from .models import Candidato,Lista
from .reportes import render_pdf
from django.http import HttpResponse

def index(request):
    lista = Lista.objects.all()[:10]    #getting the first 10 records
    context = {
        'lista': lista
    }
    return render(request, 'listadol.html', context)


class CrearLista(CreateView):
    model = Lista
    form_class = ListaForm
    template_name = 'crearl.html'
    success_url = reverse_lazy('listadol')

class ListadoLista(View):
    model = Lista
    form_class = ListaForm
    template_name = 'listadol.html'

    def get_queryset(self):
        return self.model.objects.filter(estado = True)

    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['listas'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())


class ActualizarLista(UpdateView):
    model = Lista
    form_class = ListaForm
    template_name = 'listal.html'
    success_url = reverse_lazy('listadol')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['listal'] = Lista.objects.filter(estado = True)
        return context

class EliminarLista(DeleteView):
    model = Lista

    def post(self,request,pk,*args,**kwargs):
        object = Lista.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('listadol')

class Reporte_candidato(View):
    def get(self, request, *args, **kwargs):
        candidatos = Candidato.objects.filter(estado = True)
        pdf = render_pdf("lista/candidato/reporte_candidato.html",{'candidatos':candidatos})
        return HttpResponse(pdf, content_type='application/pdf')
