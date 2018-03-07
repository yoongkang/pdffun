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
    file_data = None
    if 'signature' in request.POST:
        sigbytes = base64.b64decode(request.POST['signature'].partition(";base64,")[2])
        file_data = {'signature': ContentFile(content=sigbytes, name='signature.png')}
    form = PdfForm(request.POST or None, file_data)
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
