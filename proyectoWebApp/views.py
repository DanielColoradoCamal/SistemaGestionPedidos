from django.shortcuts import render, HttpResponse


# Create your views here.

def inicio(request):
    return render(request, 'proyectoWebApp/inicio.html')


def tienda(request):
    return render(request, 'proyectoWebApp/tienda.html')


def politica(request):
    return render(request, 'proyectoWebApp/politica.html')

def cookies(request):
    return render(request, 'proyectoWebApp/cookies.html')

def legales(request):
    return render(request, 'proyectoWebApp/legales.html')

