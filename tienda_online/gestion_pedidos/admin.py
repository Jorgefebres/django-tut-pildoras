from django.contrib import admin
from gestion_pedidos.models import Cliente, Articulo, Pedido

# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre', 'direccion')


class ArticuloAdmin(admin.ModelAdmin):
    list_filter = ('seccion',)
    list_display = ('nombre', 'seccion', 'precio')
    search_fields = ('nombre', 'seccion')


class PedidoAdmin(admin.ModelAdmin):
    list_filter = ('fecha',)
    list_display = ('numero', 'fecha')
    search_fields = ('numero', 'fecha')
    date_hierarchy = ('fecha')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Pedido, PedidoAdmin)
