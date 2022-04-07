from django.shortcuts import render, HttpResponse
from servicios.models import Servicio
from blog.models import Post, Categoria
# Create your views here.

def inicio(request):
    return render(request, 'proyectoWebApp/inicio.html')

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'proyectoWebApp/servicios.html', {'servicios':servicios})

def tienda(request):
    return render(request, 'proyectoWebApp/tienda.html')

def blog(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'proyectoWebApp/blog.html', {'post':posts,'categoria':categorias})

def contacto(request):
    return render(request, 'proyectoWebApp/contacto.html')

