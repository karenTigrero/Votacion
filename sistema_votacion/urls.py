"""sistema_votacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from sistema_votacion import views as app_views
from django.urls import path
from django.contrib.auth.decorators import login_required
from usuario.views import Login,logoutUsuario

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$', app_views.index),
    url(r'^error_image$', app_views.errorImg),
    url(r'^create_dataset$', app_views.create_dataset),
    url(r'^trainer$', app_views.trainer),
    #url(r'^eigen_train$', app_views.eigenTrain),
    url(r'^detect$', app_views.detect),
    url(r'^detect_image$', app_views.detectImage),
    url(r'^admin/', admin.site.urls),
    url(r'^crearv/', include('votante.urls')),
    url(r'^votante/', include('votante.urls')),
    url(r'^listadol/', include('lista.urls')),
    url(r'^reporte_candidato/', include('lista.urls')),

    #url(r'^usuario/', include('usuario.urls')),
    #url(r'^logout/',login_required(logoutUsuario)),

]
