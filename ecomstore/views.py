#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context


def index(request):
    if request.user.is_authenticated():
        plantilla = get_template('usuarios.html')
    else:
        plantilla = get_template('admin/admin.html')
    dict = {}

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)