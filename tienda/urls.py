from django.urls import path
from . import views


urlpatterns = [
    path('', views.tienda, name='Tienda'),
    path('categoriaProd/<int:categoria_id>/' ,views.categoriaProd, name='CategoriaProd'),
]