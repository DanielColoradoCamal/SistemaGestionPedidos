from xml.etree.ElementInclude import default_loader
from django.db import models


# Create your models here.

class CategoriaProducto(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name='categoriaProducto'
        verbose_name_plural='categoriasProductos'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=250, blank=True)
    imagen=models.ImageField(upload_to="tienda")
    precio=models.FloatField()
    disponibilidad=models.BooleanField()
    categoriasProd=models.ManyToManyField(CategoriaProducto)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre
    
