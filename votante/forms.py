from django import forms
from .models import Sexo,Votante
from django.core.files import File

#@admin.register(Sexo)
class SexoForm(forms.ModelForm):
    class Meta:
        model = Sexo
        fields = ['nombre']
        label = {
            'nombre':'nombre',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese sexo'
                }
            )
        }

class VotanteForm(forms.ModelForm):
    class Meta:
        model = Votante
        fields = ('cedula','nombre','apellido','telefono','direccion','correo','sexo_id')
        label = {
            'cedula':'cédula del votante',
            'nombre':'nombre del votante',
            'apellido':'apellido del votante',
            'telefono':'teléfono del votante',
            'direccion':'dirección del votante',
            'correo':'correo del votante',
            'sexo_id': 'sexo del votante',
            #'foto': 'f',
        }
        widgets = {
            'cedula': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese cédula del votante',
                    'type': 'number',
                    'id': 'cédula'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre del votante',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese apellido del votante',
                    'id':'apellido'
                }
            ),
            'telefono': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese teléfono del votante',
                    'id':'telefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese dirección del votante',
                    'id':'direccion'
                }
            ),
            'correo': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'type': 'email',
                    'placeholder': 'ejemplo@ejemplo.com',
                    'id':'correo'
                }
            ),
            'sexo_id': forms.Select(
                attrs = {
                    'class':'form-control',
                    'id':'sexo'
                }
            )
        }
