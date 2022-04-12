from django.urls import path
from proyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('servicios/', views.servicios, name='Servicios'),
    path('tienda/', views.tienda, name='Tienda'),
    path('contacto/', views.contacto, name='Contacto'),
    path('politica/', views.politica, name='Politica'),
    path('cookies/', views.cookies, name='Cookies'),
    path('legales/', views.legales, name='Legales')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)