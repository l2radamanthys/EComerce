#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


def generar_carrito_id():
    """
        Genera un identificador para el Carrito de Compras
    """
    caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    carrito_id_len = 50
    key = ""
    for i in range(carrito_id_len):
        key +=caracteres[randint(0, len(caracteres)-1)]
    return key


def get_carrito_id(request):
    """
        Obtiene el id del Carrito Actual
    """
    if request.session.get('carrito_id', None) != None:
        request.session['carrito_id'] = generar_carrito_id()
    return request.session['carrito_id']