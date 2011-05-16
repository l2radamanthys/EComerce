#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models


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
        return self.nombre


    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), { 'category_slug': self.slug })

        
class Producto(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=50, unique=True, help_text='unico valor del producto para la URL')
    marca = models.CharField(max_length=50)
    sku = models.CharField(help_text="Numero de Referencia", max_length=50)
    imagen = models.ImageField(upload_to="imagenes/fotos")
    precio = models.DecimalField(max_digits=9, decimal_places=2, default="0.00")
    precio_anterior = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default="0.00")
    is_bestseller = models.BooleanField(default=False) #?
    is_featured = models.BooleanField(default=False) #?
    cantidad = models.IntegerField("cantidad en stock", default=0)
    descripcion = models.TextField("descripcion del Producto")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, help_text="Ultima Modificacion")

    #categorias = models.ManyToManyField(Categoria)
    categoria = models.ForeignKey(Categoria)


    class Meta:
        db_table = 'productos'
        ordering = ['-created_at', 'nombre']


    def __unicode__(self):
        return self.nombre


    #@models.permalink
    #def get_absolute_url(self):
    #    return ('catalog_product', (), { 'product_slug': self.slug })


    def get_url_img(self):
        if self.imagen.name != "":
            return self.imagen.name
        else:
            return "imagenes/fotos/default.png"


    def precio_venta(self):
        if self.precio_anterior > self.precio:
            return self.precio
        else:
            return self.precio