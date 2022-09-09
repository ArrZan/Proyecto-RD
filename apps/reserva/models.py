from django.db import models
from apps.personal.models import Empleado, TransportadorCualificado
from apps.cliente.models import Cliente


class Plaza(models.Model):
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name = "Plaza"
        verbose_name_plural = "Plazas"
        ordering = ('id',)


class Reserva(models.Model):
    fechaReserva = models.DateTimeField("Fecha de Reserva", auto_now_add=True, auto_now=False)
    horaIngreso = models.TimeField("Hora de Ingreso", auto_now=False)
    diaIngreso = models.DateField("Día de Ingreso", auto_now=False)
    retiroDomicilio = models.BooleanField("Retiro a Domicilio", default=False)
    cedulaCliente = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE)
    cedulaEmpleado = models.ForeignKey(Empleado, verbose_name="Empleado", on_delete=models.PROTECT)
    idPlaza = models.ForeignKey(Plaza, verbose_name="Plaza a reservar", on_delete=models.PROTECT)

    def __str__(self):
        return '#{} - {} ({})'.format(self.id, self.cedulaCliente, self.fechaReserva.date())

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ('id',)

class ReservaTipoDet(models.Model):
    idTranspor = models.ForeignKey(TransportadorCualificado, verbose_name="Transportador", on_delete=models.PROTECT)
    idReserva = models.ForeignKey(Reserva, verbose_name="Reserva", on_delete=models.PROTECT)

    def __str__(self):
        return '#{} - {}'.format(self.id, self.idTranspor)

    class Meta:
        verbose_name = "Detalle de Reservación"
        verbose_name_plural = "Detalles de Reservaciones"
        ordering = ('id',)