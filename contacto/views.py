from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.

def contacto(request):
    contactoForm = ContactoForm()
    return render(request, 'contacto/contacto.html', {'contactoForm': contactoForm})