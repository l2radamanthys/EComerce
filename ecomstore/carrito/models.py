#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from catalogo.models import Producto


class CarritoItem(models.Model):
    carrito_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField(default=1)
    #fk
    producto = models.ForeignKey(Producto, unique=False)


    class Meta:
        db_table = 'carrito_items'
        ordering = ['date_added']


    def total(self):
        return self.cantidad * self.product.precio


    def nombre(self):
        return self.producto.nombre


    def precio(self):
        return self.producto.precio


    def get_absolute_url(self):
        return self.producto.get_absolute_url()


    def aumentar_cantidad(self, cantidad=0):
        self.cantidad = self.cantidad + int(cantidad)
        self.save()







