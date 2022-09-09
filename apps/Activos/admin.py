from django.contrib import admin
from apps.Activos.models import EquipoTipo, ProductoTipo, MaquinariaModelo, Producto, Equipo, Maquinaria


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('datos', 'descripcion', 'precio', 'stock', 'idProductoTipo',)

    list_per_page = 8

    list_editable = ('precio', 'stock',)

    def datos(self, obj):
        return obj.nombre.upper()


@admin.register(Maquinaria)
class MaquinariaAdmin(admin.ModelAdmin):
    list_display = ('datos', 'fechaAdquisicion', 'EstadoReponer', 'EstadoMantenimiento', 'observacion',)

    list_per_page = 10

    list_filter = ('EstadoReponer', 'EstadoMantenimiento',)

    def datos(self, obj):
        return obj.nombre.upper()


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('datos', 'estadoReponer', 'idEquipTipo',)

    # list_editable = ('estadoReponer',)

    list_per_page = 10

    list_filter = ('estadoReponer', 'idEquipTipo',)

    def datos(self, obj):
        return obj.nombre.upper()


admin.site.register(EquipoTipo)

admin.site.register(ProductoTipo)
admin.site.register(MaquinariaModelo)
