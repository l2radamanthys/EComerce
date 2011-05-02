#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context

from utils import *

def index(request):
    if request.user.is_authenticated():
        plantilla = get_template('admin/admin.html')
    else:
        plantilla = get_template('users/index.html')
    dict = generar_base_dict(request)

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)