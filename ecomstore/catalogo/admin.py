#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from catalogo import models


admin.site.register(models.Categoria)
admin.site.register(models.Producto)