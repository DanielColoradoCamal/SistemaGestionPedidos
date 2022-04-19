from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# def autenticacion(request):
#    return render(request, 'registro/registro.html')

class VistaRegistro(View):
    def get(self,request):
        form = UserCreationForm()
        return render(request,'registro/registro.html', {'form':form})
    def post(self,request):
        form= UserCreationForm(request.POST)

        if form.is_valid:   
            usuario=form.save()
            login(request,usuario)

            return redirect('Inicio')
        else:
            pass



        
