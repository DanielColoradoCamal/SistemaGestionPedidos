from django.shortcuts import render
from tienda.models import Producto, CategoriaProducto
# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/tienda.html', {'productos':productos})

def categoriaProd(request, id):
    categoriaProducto= CategoriaProducto.objects.get(id=id)
    productos= Producto.objects.filter(categoriaProdcuto=categoriaProducto)
    return render(request,'tienda/categoriaProd.html', {'productos':productos, 'categoriaProducto': categoriaProducto})
