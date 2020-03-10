from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^crearl$', views.CrearLista),
    url(r'^listadol$', views.ListadoLista),
    url(r'^editarl/(?P<id>\d+)/$', views.ActualizarLista, name= 'editarl'),
    url(r'^eliminarl/(?P<id>\d+)/$', views.EliminarLista),
    url(r'^reporte_candidato$', views.Reporte_candidato),

    #path('reporte_candidato/',login_required(Reporte_candidato.as_view()), name = 'reporte_candidato'),
]
