from django.contrib import admin

# IMPORTAMOS LOS MODELOS
from.models import Provincia, Tipo, Ingrediente, Cliente, Pedido, Platillo, Detalle, Receta

# REGISTRAMOS LOS MODELOS
admin.site.register(Provincia)
admin.site.register(Tipo)
admin.site.register(Ingrediente)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Platillo)
admin.site.register(Detalle)
admin.site.register(Receta)
