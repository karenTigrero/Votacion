from __future__ import unicode_literals

from django.contrib import admin

from .models import Votante,Sexo
admin.site.register(Votante)
admin.site.register(Sexo)
