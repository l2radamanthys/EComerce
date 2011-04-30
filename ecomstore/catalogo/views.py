#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context


from utils import *
from catalogo.models import Categoria


def agregar_categoria(request):
    """
    """
    plantilla = get_template('admin/nueva-categoria.html')
    dict = {}
    query = int(get_value(request, 'query', '0'))
    dict['query'] = query
    
    #si se hizo una consulta
    if query:
        categoria = Categoria(
            nombre = get_value(request, 'categoria', ''),
            slug = get_value(request, 'slug', ''),
            descripcion = get_value(request, 'descripcion', ''),
            meta_keywords = get_value(request, 'meta_keywords', ''),
            meta_descripcion = get_value(request, 'meta_descripcion', ''),
            is_active = True
        )
        categoria.save()
        dict['mensaje'] = "Categoria Agregada"
        dict['msj_class'] = "msj_ok"


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def listado_categorias(request):
    """
    """
    plantilla = get_template('admin/listado-categoria.html')
    dict = {}
    categorias = []
    for cat in Categoria.objects.all():
        categorias.append(cat.nombre)
        
    dict['categorias'] = categorias

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def modificar_categoria(request, sluq=""):
    plantilla = get_template('admin/nuevo-producto.html')
    dict = {}

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def borrar_categoria(request, sluq=""):
    plantilla = get_template('admin/nuevo-producto.html')
    dict = {}

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def nuevo_producto(request):
    plantilla = get_template('admin/nuevo-producto.html')
    dict = {}

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def modificar_producto(request, slug=""):
    plantilla = get_template('admin/nuevo-producto.html')
    dict = {}

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def producto_info(request, slug=""):
    plantilla = get_template('admin/nuevo-producto.html')
    dict = {}

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def listar_producto(request, slug="", pag=0):
    plantilla = get_template('admin/nuevo-producto.html')
    dict = {}

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)



