#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Listado de constantes personalizadas q se usaran en el Sistema
"""

import os


#ruta del proyecto
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
_MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MI_TEMPLATE_DIR = os.path.join(PROJECT_PATH, 'templates')

POST = "POST"
GET = "GET"

#para paginacio numero maximo de registros a mostrar por consulta
MAX_REG = 5