from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^voto/(?P<id>\d+)/$', views.voto, name='voto'),

    url(r'^crearv$', views.CrearVotante),
    url(r'^listadov$', views.ListadoVotante, name= 'listadov'),
    url(r'^editarv/(?P<id>\d+)/$', views.ActualizarVotante, name= 'editarv'),
    url(r'^eliminarv/(?P<id>\d+)/$', views.EliminarVotante)
]
