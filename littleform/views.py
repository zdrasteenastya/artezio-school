# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from .models import Junior


def index(request):
    message = '' if not request.POST.keys() else True
    return render(request, 'littleform/index.html', {'message': message})


def inquiry(request):
    form_data = {key: value for key, value in request.POST.items() if not key.startswith('csr')}
    jun = Junior(**form_data)
    jun.save()
    return redirect('index')
