from django.contrib import admin
from django.contrib.admin import AdminSite
from apps.cliente.models import Cliente, VehiculoMarca, VehiculoModelo, VehiculoCarroceria, Vehiculo

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'cedulaCliente',
        'nombres',
        'apellidos',
        'telefono',
        'correo',
        'direccion',
    )

    search_fields = ('cedulaCliente', 'apellidos',)


@admin.register(VehiculoMarca)
class VehiculoMarcaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'marca',
    )


@admin.register(VehiculoModelo)
class VehiculoModeloAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'modelo',
        'idMarca',
    )

    search_fields = ('modelo', 'idMarca',)

    list_filter = ('idMarca',)

@admin.register(VehiculoCarroceria)
class VehiculoCarroceriaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
    )

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cedulaCli',
        'idCarroceria',
        'idModelo',
        'placa',
        'añoFabri',
    )

    list_per_page = 8

    list_filter = ('idCarroceria',)

