from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    contactoForm = ContactoForm()

    if request.method =='POST':
        contactoForm = ContactoForm(data=request.POST)
        if contactoForm.is_valid():
            nombre = request.POST.get('nombre')
            correo = request.POST.get('correo') 
            mensaje = request.POST.get('mensaje')

            email = EmailMessage('Mensaje desde app gestion Pedidos',
            'El usuario {} con el correo {} \n Dejo este mensaje: \n {}'.format(nombre,correo,mensaje),'',['daniel.colorado.developer@gmail.com'],reply_to=[correo])

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, 'contacto/contacto.html', {'contactoForm': contactoForm})