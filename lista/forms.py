
from django import forms
from django.core.exceptions import ValidationError
from .models import Candidato,Lista
#from django.forms.widgets import CheckboxSelectSimple

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['cedula','nombre','apellidos','direccion']
        labels = {
            'cedula': 'Cédula del candidato',
            'nombre': 'Nombre del candidato',
            'apellidos': 'Apellidos del candidato',
            'direccion': 'Dirección',
        }
        widgets = {
            'cedula': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Introduzca cedula del candidato',
                    'type': 'number',
                    #input_type: 'number'
                    'id': 'cédula'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del candidato',
                    'id': 'nombre'
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los apellidos del candidato',
                    'id':'apellidos'
                }
            ),
            'direccion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese direccion para el candidato',
                    'id':'direccion'
                }
            )
        }
        help_texts = {
        'cedula': ('No pueden existir cedulas repetidas'),
        }

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ('nombre','candidato_id','propuesta')
        label = {
            'nombre':'nombre de la lista',
            'candidato_id': 'Candidato(s) de la Lista',
            'propuesta': 'Propuesta de la lista'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre de la Lista'
                }
            ),
            'candidato_id': forms.SelectMultiple(
                attrs = {
                    'class':'form-control'
                }
            ),
            'propuesta': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la propuesta de la Lista'
                }
            )
        }
