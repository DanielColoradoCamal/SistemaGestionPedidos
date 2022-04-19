from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
# def autenticacion(request):
#    return render(request, 'registro/registro.html')

class VistaRegistro(View):
    def get(self,request):
        form = UserCreationForm()
        return render(request,'registro/registro.html', {'form':form})
    def post(self,request):
        form= UserCreationForm(request.POST)

        if form.is_valid():   
            usuario=form.save()
            login(request,usuario)

            return redirect('Inicio')
        else:
            for mensaje in form.error_messages:
                messages.error(request, form.error_messages[mensaje])
            return render(request,'registro/registro.html', {'form':form})

def cerrar_sesion(request):
    logout(request)
    return redirect('Inicio')

def loguear(request):
    if request.method=='POST':   
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            usuario=authenticate(username=nombre_usuario,password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Inicio')
            else:
                messages.error(request, 'Usuario no valido')
        else:
            messages.error(request, 'Usuario no valido')

    form=AuthenticationForm()
    return render(request,'login/login.html', {'form':form})
    


        
