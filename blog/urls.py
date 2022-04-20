from django.urls import path
from . import views



urlpatterns = [
    path('', views.blog, name='Blog'),
    path('categoria/<int:categoria_id>/' ,views.categoria, name='Categoria'),
    path('post/<int:id>/',views.post, name='Post'),
]