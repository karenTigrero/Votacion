from io import BytesIO
from .models import Candidato
from reportlab.lib.pagesizes import A4
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from reportlab.lib.styles import ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from django.urls import reverse_lazy
from xhtml2pdf import pisa
from reportlab.platypus import (
        Paragraph,
        Table,
        SimpleDocTemplate,
        Spacer,
        TableStyle,
        Paragraph)

def render_pdf(url_template, contexto={}):
    #template_name = 'lista/candidato/reporte_candidato.html'
    template = get_template('lista/candidato/reporte_candidato.html')
    #success_url = reverse_lazy('lista:reporte_candidato')
    html = template.render(contexto)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type = 'application/pdf')
    return None
