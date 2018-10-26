from django.db import models

# Create your models here.

class Producto(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=30)
	cantidad = models.IntegerField(default = 0)
	precio = models.FloatField(default = 0)

	def __str__(self):
		return '{}'.format(self.id)

class Categoria1(models.Model):
	producto = models.ForeignKey(Producto, null = True, blank = True, on_delete = models.CASCADE)

class Categoria2(models.Model):
	producto = models.ForeignKey(Producto, null = True, blank = True, on_delete = models.CASCADE)
