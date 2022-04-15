from django.urls import path
from . import views


urlpatterns = [
    path('', views.tienda, name='Tienda'),
    path('categoriaProd/<int:id>/' ,views.categoriaProd, name='Categoria'),
]