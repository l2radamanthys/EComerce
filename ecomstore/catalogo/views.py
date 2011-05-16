#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context

from catalogo.models import Categoria, Producto
from utils import *
from constantes import MAX_REG


def agregar_categoria(request):
    """
    """
    plantilla = get_template('admin/nueva-categoria.html')
    dict = generar_base_dict(request)
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
    dict = generar_base_dict(request)

    categorias = []
    for cat in Categoria.objects.all():
        categorias.append(cat.nombre)
    dict['categorias'] = categorias

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def modificar_categoria(request, sluq=""):
    plantilla = get_template('admin/nuevo-producto.html')
    dict = generar_base_dict(request)

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def borrar_categoria(request, sluq=""):
    plantilla = get_template('admin/nuevo-producto.html')
    dict = generar_base_dict(request)

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def nuevo_producto(request):
    plantilla = get_template('admin/nuevo-producto.html')
    dict = generar_base_dict(request)
    query = int(get_value(request, 'query', '0'))
    dict['query'] = query

     #listo todas las categorias disponibles para ser añadidas al select
    categorias = []
    for cat in Categoria.objects.all():
        categorias.append(cat.nombre)
    dict['categorias'] = categorias

    #si se envio una consulta agr
    if query:      
        producto = Producto(
            nombre = get_value(request, "nombre", ""),
            slug = get_value(request, "slug", ""),
            marca = get_value(request, "marca", ""),
            sku = get_value(request, "sku", ""),
            imagen = request.FILES["imagen"],
            precio = get_value(request, "precio", "0.00"),
            precio_anterior = get_value(request, "precio", "0.00"),
            is_bestseller = get_value(request, "is_bestseller", False),
            is_featured = get_value(request, "is_featured", False),
            descripcion = get_value(request, "descripcion", ""),
            is_active = get_value(request, "is_active", True),
            categoria = Categoria.objects.get(nombre=get_value(request, "categoria", ""))
        )
        producto.save()

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def modificar_producto(request, slug=""):
    plantilla = get_template('admin/nuevo-producto.html')
    dict = generar_base_dict(request)

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def producto_info(request, prod_id="-1"):
    plantilla = get_template('users/producto-info.html')
    dict = generar_base_dict(request)

    prod_id = int(prod_id)
    if prod_id != -1:
        producto = Producto.objects.get(id=prod_id)
        dict["nombre"] = producto.nombre
        dict["marca"] = producto.marca
        dict["categoria"] = producto.categoria.nombre
        dict["precio_anterior"] = producto.precio_anterior
        dict["precio"] = producto.precio
        dict["descripcion"] = producto.descripcion
        dict["imagen"] = producto.get_url_img()
        dict["prod_id"] = producto.id

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def productos_listado_adm(request, prod_id=""):
    plantilla = get_template('admin/listado-productos.html')
    dict = generar_base_dict(request)

    #productos = []
    #for prod in Productos.objects.all():
    #    productos.append([prod.nombre, prod.get_url_img(), prod.precio])
    #dict["productos"] = productos

    categorias = []
    for cat in Categoria.objects.all():
        categorias.append( cat.nombre)
    dict["categorias"] = categorias

    #pregunto por q categoria va a realizar la busqueda
    categoria = get_GET_value(request, "cat", "")
    dict["categoria"] = categoria

    if categoria == "":
        _productos = Producto.objects.all()
    else:
        _productos = Producto.objects.filter(categoria__nombre=categoria)

    productos = []
    for prod in _productos:
        productos.append([prod.id, prod.nombre, prod.categoria.nombre])

    dict["productos"] = productos


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def productos_listado(request):
    plantilla = get_template('users/listado-productos.html')
    dict = generar_base_dict(request)

    categorias = []
    for cat in Categoria.objects.all():
        categorias.append( cat.nombre)
    dict["categorias"] = categorias

    #pregunto por q categoria va a realizar la busqueda
    categoria = get_GET_value(request, "cat", "")
    dict["categoria"] = categoria
    
    if categoria == "":
        _productos = Producto.objects.all()
    else:
        _productos = Producto.objects.filter(categoria__nombre=categoria)


    pag = int(get_GET_value(request, "pag", "0"))
    num_reg = len(_productos)
    num_pag = num_reg / MAX_REG
    if pag > num_pag:
        pag = num_pag
    offset = pag * MAX_REG
    if offset < num_pag:
        offset = num_pag
    
    productos = []
    for prod in _productos:
        productos.append([prod.id, prod.nombre, prod.get_url_img(), prod.precio, prod.descripcion])

    dict["productos"] = productos

    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)
