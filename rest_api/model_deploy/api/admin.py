from django.contrib import admin

# Register your models here
from .models import Autores, Libros, PedidoCliente, Categorias, Clientes, LibroPorAutor

admin.site.register(Autores)
admin.site.register(Libros)
admin.site.register(PedidoCliente)
admin.site.register(Categorias)
admin.site.register(Clientes)
admin.site.register(LibroPorAutor)