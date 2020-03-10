from __future__ import unicode_literals
from django.db import models

class Sexo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'
        ordering = ['nombre']

    def __str__(self):
        return '%s' % (self.nombre)

class Votante(models.Model):
    id = models.AutoField(primary_key = True)
    cedula = models.IntegerField(unique=True, blank = False, null= False)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    apellido = models.CharField(max_length = 220, blank = False, null = False)
    telefono = models.CharField(max_length = 100, blank = False, null = False)
    direccion = models.TextField(max_length = 220, blank = False, null = False)
    correo = models.CharField(max_length = 220,blank = False,null = False)
    sexo_id = models.ManyToManyField(Sexo)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Votante'
        verbose_name_plural = 'Votantes'
        ordering = ['apellido']

    def __str__(self):
        return '%s %s' % (self.apellido, self.nombre)
