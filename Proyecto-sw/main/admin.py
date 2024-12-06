from django.contrib import admin
from .models import *


# Registro de modelos en el panel de administración
admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Pedidos)
admin.site.register(DetallePedido)
admin.site.register(Pagos)
admin.site.register(CarritoVentas)
admin.site.register(DetalleCarrito)
admin.site.register(Trabajadores)
admin.site.register(RolesTrabajadores)
admin.site.register(Categoria)