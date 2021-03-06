from django.shortcuts import render
from tienda.models import Producto, CategoriaProducto
# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/tienda.html', {'productos':productos})

def categoriaProd(request, categoria_id):
    categoriaProducto= CategoriaProducto.objects.get(id=categoria_id)
    productos= Producto.objects.filter(categoriaProducto=categoriaProducto)
    return render(request,'tienda/categoriaProd.html', {'productos':productos, 'categoriaProducto': categoriaProducto})
