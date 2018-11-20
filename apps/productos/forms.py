from django import forms
from apps.productos.models import Producto, Categoria1, Categoria2

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = [
			'nombre',
			'descripcion',
			'cantidad',
			'precio'
		]

		labels = {
			'nombre' : 'Nombre',
			'descripcion' : 'Descripcion',
			'cantidad' : 'Cantidad',
			'precio' : 'Precio'
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
			'descripcion' : forms.TextInput(attrs={'class' : 'form-control'}),
			'cantidad' : forms.TextInput(attrs={'class' : 'form-control'}),
			'precio' : forms.TextInput(attrs={'class' : 'form-control'}),
		}
class VentasForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = [
			'nombre',
			'precio',
			'cantidad',
		]

		labels = {
			'nombre' : 'Nombre',
			'precio' : 'Precio Unitario',
			'cantidad' : 'Cantidad a Comprar',
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class' : 'form-control', 'readonly':'readonly'}),
			'precio' : forms.TextInput(attrs={'class' : 'form-control', 'readonly':'readonly'}),
			'cantidad' : forms.TextInput(attrs={'class' : 'form-control'}),
		}


class Categoria1Form(forms.ModelForm):
	class Meta:
		model = Categoria1
		fields = [
			'producto',
		]

		labels = {
			'producto' : 'ID de Producto',
		}

		widgets = {
			'producto' : forms.TextInput(attrs={'class' : 'form-control'}),
		}


class Categoria2Form(forms.ModelForm):
	class Meta:
		model = Categoria2
		fields = [
			'producto',
		]

		labels = {
			'producto' : 'ID de Producto',
		}

		widgets = {
			'producto' : forms.TextInput(attrs={'class' : 'form-control'}),
		}