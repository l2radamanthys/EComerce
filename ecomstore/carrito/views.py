#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context

from catalogo.models import Categoria, Producto
from carrito.models import CarritoItem
from utils import *


def mostrar_carrito(request):
    """
    """
    plantilla = get_template('users/carrito.html')
    dict = generar_base_dict(request)

    _carrito_id = get_carrito_id(request)
    
    carrito = []
    for item in CarritoItem.objects.filter(carrito_id=_carrito_id):
        productos.append([item.producto.id, item.producto.nombre, item.cantidad])
    dict["carrito"] = carrito


    contexto = Context(dict)
    html = plantilla.render(contexto)
    return HttpResponse(html)


def agregar_al_carrito(request):
    """
    """
    _carrito_id = get_carrito_id(request)
    prod_id = int(get_POST_value(request, "prod_id", "-1"))
    _cantidad = int(get_POST_value(request, "cantidad", "0"))

    _producto = Producto.objects.get(id=prod_id)
    carrito_item = CarritoItem(
        carrito_id = _carrito_id,
        cantidad = _cantidad,
        producto = _producto
    )
    carrito_item.save()

    return HttpResponseRedirect('/carrito/mostrar/')
    



def sacar_del_carrito(request, prod_id="-1"):
    pass


def cambiar_cantidad(request, prod_id="-1"):
    pass


def vaciar_carrito(request, prod_id="-1"):
    pass

