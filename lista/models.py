from django.db import models

class Candidato(models.Model):
    id = models.AutoField(primary_key = True)
    cedula = models.IntegerField(unique=True, blank = False, null= False)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    apellidos = models.CharField(max_length = 220, blank = False, null = False)
    direccion = models.TextField(blank = False,null = False)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'
        ordering = ['apellidos']

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)

    def clean_cedula(self):
        ced = self.cleaned_data['cedula']

        valores = [ int(ced[x]) * (2 - x % 2) for x in range(9) ]
        suma = sum(map(lambda x: x > 9 and x - 9 or x, valores))
        veri = 10 - (suma - (10 * (suma / 10)))
        if int(ced[9]) == int(str(veri)[-1:]):
            return ced
        else:
            raise forms.ValidationError(_("La Cédula introducida no es válida"))

class Lista(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Lista', max_length = 255, blank = False, null = False)
    propuesta = models.TextField('Propuesta', blank = False, null = False)
    candidato_id = models.ManyToManyField(Candidato)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    class Meta:
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'
        ordering = ['nombre']

    def __str__(self):
        return '%s' % (self.nombre)
