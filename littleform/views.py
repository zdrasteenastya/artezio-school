# -*- coding: utf-8 -*-
import re

from django.shortcuts import render
from .models import Junior


def index(request):
    return render(request, 'littleform/index.html')


def inquiry(request):
    args = request.POST
    if args['g-recaptcha-response']:
        if not all([
            re.match('^([0-9\(\)\/\+ \-]*)$', args['phone_number']),
            len(''.join(re.findall('\d+', args['phone_number']))) == 11
        ]):
            return render_main_page(request, {'phone_number': True})
        if not re.search('(^|\s)[\w.]+@([\w]+\.)+[\w]{2,6}(\s|$)', args['email']):
            return render_main_page(request, {'email': True})

        form_data = {key: value for key, value in request.POST.items() if not key.startswith(('csr', 'g-recaptcha'))}
        try:
            form_data.update({'file': request.FILES['file']})
        except Exception:
            pass
        jun = Junior(**form_data)
        jun.save()


        return render_main_page(request, {'success': True})
    else:
        return render_main_page(request, {'recaptcha': True})


def render_main_page(request, message):
    return render(
        request,
        'littleform/index.html',
        message
    )