#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context


def index(request):
    plantilla = get_template('base.html')
    dict = {}

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)