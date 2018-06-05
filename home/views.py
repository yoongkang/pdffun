from django.shortcuts import render
from django import forms
from django.http.response import Http404, JsonResponse
from django.core.files.base import ContentFile
from pdfjinja import PdfJinja
from io import BytesIO
from django.conf import settings

import os
import base64

from .models import Invoice


class PdfForm(forms.Form):
    CITIES = (
        ('sydney', 'Sydney'),
        ('melbourne', 'Melbourne'),
        ('adelaide', 'Adelaide'),
        ('perth', 'Perth'),
    )
    LANGUAGES = (
        ('python', 'Python'),
        ('ruby', 'Ruby'),
        ('javascript', 'JavaScript'),
    )
    name = forms.CharField(max_length=128)
    address = forms.CharField(max_length=256)
    city = forms.MultipleChoiceField(choices=CITIES)
    language = forms.ChoiceField(choices=LANGUAGES)
    signature = forms.ImageField(required=False)


def the_form(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})
    form = PdfForm(request.POST, request.FILES)
    if form.is_valid():
        data = form.cleaned_data.copy()
        for city in ['sydney', 'melbourne', 'adelaide', 'perth']:
            data[city] = city in data['city']
        mypdf = PdfJinja('home/static/home/sydjango3.pdf')
        pdfout = mypdf(data)
        b = BytesIO(b'')
        pdfout.write(b)
        b.seek(0)
        invoice = Invoice.objects.create()
        invoice.document.save('mypdf.pdf', ContentFile(b.read()))
        return JsonResponse({'redirect_url': invoice.document.url })
    return render(request, 'index.html', {'form': form})
