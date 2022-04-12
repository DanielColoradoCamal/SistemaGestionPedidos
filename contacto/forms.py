from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, required=True)
    correo = forms.CharField(label='Correo electronico', max_length=100, required=True)
    mensaje = forms.CharField(label='Mensaje', max_length=500)