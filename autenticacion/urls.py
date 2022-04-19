from django.urls import path
from .views import VistaRegistro



urlpatterns = [
    path('', VistaRegistro.as_view(), name='Autenticacion'),
]