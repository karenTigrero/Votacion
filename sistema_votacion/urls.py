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

from django.conf.urls import url, include
from django.contrib import admin
from sistema_votacion import views as app_views
from django.urls import path
from django.contrib.auth.decorators import login_required
from usuario.views import Login,logoutUsuario

url(r'^admin/', admin.site.urls),
url(r'^$', app_views.index),
url(r'^error_image$', app_views.errorImg),
url(r'^create_dataset$', app_views.create_dataset),
url(r'^trainer$', app_views.trainer),
#url(r'^eigen_train$', app_views.eigenTrain),
url(r'^detect$', app_views.detect),
url(r'^detect_image$', app_views.detectImage),
path('error_image/',login_required(errorImg.as_view()), name = 'error_image'),
path('create_dataset/',login_required(create_dataset.as_view()), name = 'create_dataset'),
path('trainer/',login_required(trainer.as_view()), name = 'trainer'),
path('detect/',login_required(detect.as_view()), name = 'detect'),
path('detect_image/',login_required(detectImage.as_view()), name = 'detect_image'),
url(r'^votante/', include('votante.urls')),
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
#import Inicio from lista.views
from sistema_votacion import views as app_views
from usuario.views import Login,logoutUsuario
from lista.views import Inicio
from votante.views import Inicio
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_required(Inicio.as_view()), name = 'index'),
    url(r'^error_image$', app_views.errorImg),
    url(r'^create_dataset$', app_views.create_dataset),
    url(r'^trainer$', app_views.trainer),
    url(r'^detect$', app_views.detect),
    url(r'^detect_image$', app_views.detectImage),
    path('votante/',include(('votante.urls','votante'))),
    path('lista/',include(('lista.urls','lista'))),
    path('logout/',login_required(logoutUsuario),name = 'logout'),
]
