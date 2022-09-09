from django.contrib import admin
from apps.servicio.models import ServicioCab, ServicioTipo, ServicioDomicilio, ServicioCalificacion, \
    ServicioTipoDet, ServicioEquiDet, ServicioMaquDet, ServicioProdDet, ServicioTrabDet

admin.site.register(ServicioCab)
admin.site.register(ServicioTipo)
admin.site.register(ServicioDomicilio)
admin.site.register(ServicioCalificacion)
admin.site.register(ServicioTipoDet)
admin.site.register(ServicioEquiDet)
admin.site.register(ServicioMaquDet)
admin.site.register(ServicioProdDet)
admin.site.register(ServicioTrabDet)
