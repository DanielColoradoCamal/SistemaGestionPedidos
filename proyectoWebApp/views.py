from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

# Create your views here.

def inicio(request):
    return render(request, 'proyectoWebApp/inicio.html')

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'proyectoWebApp/servicios.html', {'servicios':servicios})

def tienda(request):
    return render(request, 'proyectoWebApp/tienda.html')



def contacto(request):
    return render(request, 'proyectoWebApp/contacto.html')

def politica(request):
    return render(request, 'proyectoWebApp/politica.html')

def cookies(request):
    return render(request, 'proyectoWebApp/cookies.html')

def legales(request):
    return render(request, 'proyectoWebApp/legales.html')

