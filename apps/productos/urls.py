from django.urls import path
from apps.productos.views import principal, listado, categoria, Producto, categorias, nuevoRegistro, editarRegistro, eliminarRegistro, nvoC1, nvoC2, editC1, editC2, elimC1, elimC2, Ventas, ventForm, errorCant

app_name = 'productos'
urlpatterns = [
    #path('principal', principal, name="principal"),
    path('', principal),
    path('categoria', categorias),
    path('categorias', categorias, name="verCategorias"),
    path('productos', Producto.as_view(), name="verProductos"),
    path('principal', Ventas.as_view(), name="principal"),
    path('errorCant', errorCant, name="errorCantidad"),

    path('ventaProducto/<idProducto>', ventForm, name="ventF"),
    path('nuevoRegistro', nuevoRegistro, name="nuevoRegistro"),
    path('editarRegistro/<idProducto>', editarRegistro, name="editarRegistro"),
    path('eliminarRegistro/<idProducto>', eliminarRegistro, name="eliminarRegistro"),

    path('nvoC1', nvoC1, name="nvoC1"),
    path('editC1/<idC>', editC1, name="editC1"),
    path('elimC1/<idC>', elimC1, name="elimC1"),

    path('nvoC2', nvoC2, name="nvoC2"),
    path('editC2/<idC>', editC2, name="editC2"),
    path('elimC2/<idC>', elimC2, name="elimC2"),
]