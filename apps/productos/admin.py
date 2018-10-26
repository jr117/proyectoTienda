from django.contrib import admin
from apps.productos.models import Producto, Categoria1, Categoria2

# Register your models here.

admin.site.register(Producto)
admin.site.register(Categoria1)
admin.site.register(Categoria2)