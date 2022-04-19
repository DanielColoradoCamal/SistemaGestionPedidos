from django.urls import path
from .views import VistaRegistro, cerrar_sesion, loguear



urlpatterns = [
    path('', VistaRegistro.as_view(), name='Autenticacion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('loguear', loguear, name='loguear'),
]