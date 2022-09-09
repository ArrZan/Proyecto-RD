from django.contrib import admin
from apps.reserva.models import Plaza, Reserva, ReservaTipoDet

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('fechaReserva','horaIngreso','diaIngreso','cedulaCliente', 'retiroDomicilio','idPlaza',)


@admin.register(ReservaTipoDet)
class ReservaTipoDetAdmin(admin.ModelAdmin):
    list_display = ('id','idTranspor','idReserva',)

    list_filter = ('idTranspor',)



admin.site.register(Plaza)