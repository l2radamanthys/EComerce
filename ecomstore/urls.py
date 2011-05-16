#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#propios
from settings import MEDIA_ROOT
import views
import catalogo.views as catalogo_views
import carrito.views as carrito_views


urlpatterns = patterns('',
    # Example:
    # (r'^ecomstore/', include('ecomstore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    #archivos staticos
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT, 'show_indexes': True }),

    #urls
    (r'^/?$', views.index),

    ## - catalgo - adm
    # categorias
    (r'^catalogo/producto/agregar-categoria/$', catalogo_views.agregar_categoria),
    (r'^catalogo/producto/listado-categorias/$', catalogo_views.listado_categorias),

    #productos
    (r'^catalogo/producto/nuevo/$', catalogo_views.nuevo_producto),
    (r'^catalogo/producto/listado-adm/$', catalogo_views.productos_listado_adm),

    ## - catalgo - users
    (r'^catalogo/producto/info/(\d{1,2})/$', catalogo_views.producto_info),
    (r'^catalogo/producto/info/$', catalogo_views.producto_info),
    (r'^catalogo/producto/listado/$', catalogo_views.productos_listado),

    ## carrito
    (r'^carrito/agregar-al-carrito/$', carrito_views.agregar_al_carrito),
    (r'^carrito/mostrar/$', carrito_views.mostrar_carrito),
    #(r'^carrito/generar_ticket/$', carrito_views.generar_ticket),
    

    ## - usuarios - ##
    #(r'^accounts/login/$', generics_views.login),
    #(r'^accounts/logout/$', generics_views.logout),

)
