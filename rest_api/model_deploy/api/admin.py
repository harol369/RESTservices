from django.contrib import admin
from .models import Autores,Libros,PedidoCliente,Categorias,Clientes,LibroPorAutor
# Register your models here.

admin.site.register(Categorias)
admin.site.register(Libros)
admin.site.register(Autores)
admin.site.register(PedidoCliente)
admin.site.register(Clientes)
admin.site.register(LibroPorAutor)
