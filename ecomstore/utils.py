#!/usr/bin/env python
# -*- coding: utf-8 -*-


from random import randint
from constantes import *


def generar_carrito_id():
    """
        Genera un identificador para el Carrito de Compras
    """
    caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    carrito_id_len = 50
    key = ""
    for i in range(carrito_id_len):
        key += caracteres[randint(0, len(caracteres)-1)]
    return key


def get_carrito_id(request):
    """
        Obtiene el id del Carrito Actual
    """
    if request.session.get('carrito_id', None) != None:
        request.session['carrito_id'] = generar_carrito_id()
    return request.session['carrito_id']


def get_GET_value(request, key='', default='', blank=''):
    value = request.POST.get(key, default)
    if value == '':
        value = blank
    return value


def get_POST_value(request, key='', default='', blank=''):
     value = request.POST.get(key, default)
     if value == '':
        value = blank
     return value


def get_value(request=None, key='', default='', blank='', method=POST):
    if method == POST:
        return get_POST_value(request, key, default, blank)
    else:
        return get_GET_value(request, key, default, blank)
