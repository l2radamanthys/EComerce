#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context


from utils import *
from catalogo.models import Categoria


def agregar_categoria(request):
    if not(request.user.is_authenticated()):
        plantilla = get_template('usuarios.html')
    else:
        plantilla = get_template('admin/nueva-categoria.html')
    dict = {}

    query = int(get_value(request, 'q', '0'))
    
    #si se hizo una consulta
    if query:
        nombre = get_value(request, 'categoria', '')
        slug = get_value(request, 'slug', '')
        descripcion = get_value(request, 'descripcion', '')
        meta_key = get_value(request, 'meta_keywords', '')
        meta_desc = get_value(request, 'meta_descripcion', '')

        categoria = Categoria(nombre, slug, descripcion, meta_key, meta_desc)
        categoria.save()
        
    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def listado_categorias(request):
    plantilla = get_template('admin/listado-categoria.html')
    dict = {}
    categorias = []
    for cat in Categoria.objects.all():
        categorias.append(cat.nombre)

    dict['categorias'] = categorias

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def borrar_categoria(request, sluq=""):
    pass


def nuevo_producto(request):
    pass


def modificar_producto(request, slug=""):
    pass


def producto_info(request, slug=""):
    pass


def listar_producto(request, slug="", pag=0):
    pass



