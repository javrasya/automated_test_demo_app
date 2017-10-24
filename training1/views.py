# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django import forms
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render

from training1.models import Service1, Log, HIZMET_LISTELEME_CODE


# Create your views here.


class ListSearchForm(forms.Form):
    uyariTipi = forms.CharField(label="Uyari Tipi", max_length=100)
    uyeAdi = forms.CharField(label="Uye Adi", max_length=100)
    kontrolVeriTipi = forms.CharField(label="Kontrol Veri Tipi", max_length=100)


@login_required(login_url="/admin/login")
def list(request):
    context = {}
    form = None
    if request.method == "GET":
        form = ListSearchForm()

    elif request.method == "POST":
        form = ListSearchForm(request.POST)
        if form.is_valid():
            services = Service1.objects.all()
            log = Log.objects.create(
                alt_module_name=HIZMET_LISTELEME_CODE,
                user=request.user,
                input_detail=json.dumps(form.cleaned_data),
                output_detail=serializers.serialize("json", services)

            )
            context['actionCode'] = log.action_code
            context['services'] = services

    context['form'] = form

    return render(request, 'list.html', context)
