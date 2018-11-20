from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from apps.productos.models import Producto as PR
from apps.productos.models import Categoria1, Categoria2
from apps.productos.forms import ProductoForm, Categoria1Form, Categoria2Form, VentasForm

# Create your views here.

def principal(request):
	return render(request, 'base/index.html')

def errorCant(request):
	return render(request, 'productos/err.html')

def listado(request):
	contexto = {
		'productos': PR.objects.all()
	}
	return render(request, 'productos/index.html', contexto)

def categoria(request): 
	contexto = {
		'categoria1': Categoria1.objects.all(),
		'categoria2': Categoria2.objects.all()
	}
	return render(request, 'productos/paginaEspecial.html', contexto)

def categorias(request):
	contexto = {
		'categoria1': Categoria1.objects.all(),
		'categoria2': Categoria2.objects.all()
	}
	return render(request, 'productos/pagCat.html', contexto)

class Producto(ListView):
	model = PR
	queryset = PR.objects.all()
	template_name = 'productos/pagProd.html'

class Ventas(ListView):
	model = PR
	queryset = PR.objects.all()
	template_name = 'productos/pagVentas.html'

#VIEWS PARA AGREGAR, EDITAR Y ELIMINAR PRODUCTOS

def nuevoRegistro(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('productos:verProductos')
	else:
		form = ProductoForm()
	return render(request, 'productos/productoFormulario.html', {'form' : form})

def editarRegistro(request, idProducto):
	producto = PR.objects.get(id = idProducto)
	if (request.method == 'GET'):
		form = ProductoForm(instance = producto)
	else:
		form = ProductoForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
		return redirect('productos:verProductos')
	return render(request, 'productos/productoFormulario.html', {'form' : form})

def ventForm(request, idProducto):
	producto = PR.objects.get(id = idProducto)
	cant = producto.cantidad
	producto.cantidad = 0
	if (request.method == 'GET'):
		form = VentasForm(instance = producto)
	else:
		form = VentasForm(request.POST, instance=producto)
		if form.is_valid():
			precio = producto.cantidad
			producto.cantidad = cant - producto.cantidad
			if producto.cantidad < 0:
				return redirect('productos:errorCantidad')
			form.save()
		precio = float(precio) * producto.precio
		contexto = {'precio': precio}
		return render(request, 'productos/pago.html', contexto)
		return redirect('productos:principal')
	return render(request, 'productos/ventaFormulario.html', {'form' : form})

def eliminarRegistro(request, idProducto):
	producto =  PR.objects.get(id = idProducto)
	if (request.method == 'GET'):
		form = ProductoForm(instance = producto)
	else:
		form = ProductoForm(request.POST, instance=producto)
		if form.is_valid():
			producto.delete()
		return redirect('productos:verProductos')
	return render(request, 'productos/borraProducto.html', {'form' : form})



#VIEWS PARA AGREGAR, EDITAR Y ELIMINAR PRODUCTOS DE CATEGORIA 1

def nvoC1(request):
	if request.method == 'POST':
		form = Categoria1Form(request.POST)
		if form.is_valid():
			form.save()
		return redirect('productos:verCategorias')
	else:
		form = Categoria1Form()
	return render(request, 'productos/productoFormulario.html', {'form' : form})

def editC1(request, idC):
	categoria = Categoria1.objects.get(id = idC)
	if (request.method == 'GET'):
		form = Categoria1Form(instance = categoria)
	else:
		form = Categoria1Form(request.POST, instance=categoria)
		if form.is_valid():
			form.save()
		return redirect('productos:verCategorias')
	return render(request, 'productos/productoFormulario.html', {'form' : form})

def elimC1(request, idC):
	categoria =  Categoria1.objects.get(id = idC)
	if (request.method == 'GET'):
		form = Categoria1Form(instance = categoria)
	else:
		form = Categoria1Form(request.POST, instance=categoria)
		if form.is_valid():
			categoria.delete()
		return redirect('productos:verCategorias')
	return render(request, 'productos/borraProducto.html', {'form' : form})



#VIEWS PARA AGREGAR, EDITAR Y ELIMINAR PRODUCTOS DE CATEGORIA 2

def nvoC2(request):
	if request.method == 'POST':
		form = Categoria2Form(request.POST)
		if form.is_valid():
			form.save()
		return redirect('productos:verCategorias')
	else:
		form = Categoria2Form()
	return render(request, 'productos/productoFormulario.html', {'form' : form})

def editC2(request, idC):
	categoria = Categoria2.objects.get(id = idC)
	if (request.method == 'GET'):
		form = Categoria2Form(instance = categoria)
	else:
		form = Categoria2Form(request.POST, instance=categoria)
		if form.is_valid():
			form.save()
		return redirect('productos:verCategorias')
	return render(request, 'productos/productoFormulario.html', {'form' : form})

def elimC2(request, idC):
	categoria =  Categoria2.objects.get(id = idC)
	if (request.method == 'GET'):
		form = Categoria2Form(instance = categoria)
	else:
		form = Categoria2Form(request.POST, instance=categoria)
		if form.is_valid():
			categoria.delete()
		return redirect('productos:verCategorias')
	return render(request, 'productos/borraProducto.html', {'form' : form})
