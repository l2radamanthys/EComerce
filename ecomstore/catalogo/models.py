#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='unico valor del producto para la URL')
    descripcion = models.TextField()
    meta_keywords = models.CharField(max_length=255, help_text='Coma Separado de palabras claves para metatags')
    meta_descripcion = models.CharField(max_length=255, help_text='descripcion para metatags')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, help_text="Ultima Modificacion")


    class Meta:
        db_table = 'categorias' #explicita el nombre de la tabla
        ordering = ['-created_at'] #ordenamiento
        verbose_name_plural = 'Categorias' #nombre en plural estendido por django


    def __unicode__(self):
        return self.name


    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), { 'category_slug': self.slug })

        
class Producto(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=50, unique=True, help_text='unico valor del producto para la URL')
    marca = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    imagen = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    precio_anterior = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    is_bestseller = models.BooleanField(default=False) #?
    is_featured = models.BooleanField(default=False) #?
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, help_text="Ultima Modificacion")
    
    #
    categorias = models.ManyToManyField(Categoria)


    class Meta:
        db_table = 'productos'
        ordering = ['-created_at']


    def __unicode__(self):
        return self.name


    @models.permalink
    def get_absolute_url(self):
        return ('catalog_product', (), { 'product_slug': self.slug })


    def precio_venta(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None