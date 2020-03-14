from django.conf.urls import url
from . import views
from .views import *
from django.urls import path
from django.contrib.auth.decorators import login_required
app_name = 'lista'

urlpatterns = [

    path('listadol/',login_required(ListadoLista.as_view()), name = 'listadol'),
    path('crearl/',login_required(CrearLista.as_view()), name = 'crearl'),

]
