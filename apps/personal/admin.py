from django.contrib import admin
from apps.personal.models import Empleado, Cargo, Contratacion, ContratoTipo, TransportadorCualificado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'cedulaEmp',
        'nombres',
        'apellidos',
        'telefono',
        'correo',
        'cargo',
    )

    list_per_page = 8

    search_fields = ('cedulaCliente', 'apellidos',)

    list_filter = ('cargo',)

@admin.register(ContratoTipo)
class ContratoTipoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'contrato',
        'tiempo',
    )

@admin.register(Contratacion)
class ContratacionAdmin(admin.ModelAdmin):
    list_display = ('fechaContrato','fechaInicio','cedulaEmp','cargo')


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('funcion', 'sueldo',)



admin.site.register(TransportadorCualificado)