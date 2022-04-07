from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class CategoriaAdmin():
    pass

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Post, PostAdmin)