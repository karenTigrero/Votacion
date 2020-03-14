from django.conf.urls import url
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import *
app_name = 'votante'

urlpatterns = [
    #path('voto/<int:id>/',login_required(voto.as_view()), name = 'voto'),
    path('crearv/',login_required(CrearVotante.as_view()), name = 'crearv'),
    #path('crearv/',views.CrearVotante, name = 'crearv'),
    path('listadov/',login_required(ListadoVotante.as_view()), name = 'listadov'),

    url(r'^voto/(?P<id>\d+)/$', views.voto, name='voto'),


]
