from django.db import models
from django.utils.timezone import now

from apps.reserva.models import Plaza
from apps.cliente.models import Vehiculo, Cliente
from apps.venta.models import FormaPago
from apps.personal.models import TransportadorCualificado, Empleado
from apps.Activos.models import Producto, Equipo, Maquinaria

varFac = "Factura de Servicio"


class ServicioCab(models.Model):
    idVehiculo = models.ForeignKey(Vehiculo, verbose_name="Vehículo", on_delete=models.PROTECT)
    fechaFactura = models.DateTimeField(auto_now=False, default=now)
    horaEntrada = models.TimeField("Hora de Entrada", auto_now=False)
    horaSalida = models.TimeField("Hora de Entrada", auto_now=True, null=True)
    kilometraje = models.PositiveSmallIntegerField("Kilometraje", )
    kmProx = models.PositiveSmallIntegerField("Proximo Kilometraje")
    valorTotal = models.DecimalField("Total a pagar", max_digits=8, decimal_places=2)
    tiempoEstimado = models.CharField("Tiempo estimado", max_length=35, blank=True)
    idPlaza = models.ForeignKey(Plaza, verbose_name="Plaza usada", on_delete=models.PROTECT)
    idFormaPago = models.ForeignKey(FormaPago, verbose_name="Forma de Pag", on_delete=models.PROTECT)

    def __str__(self):
        return '{} - (${})'.format(self.idVehiculo, self.valorTotal)

    class Meta:
        verbose_name = "Factura de Servicio"
        verbose_name_plural = "Facturas de Servicios"
        ordering = ('fechaFactura',)


class ServicioTipo(models.Model):
    descripcion = models.CharField(max_length=150, unique=True)
    precio = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        verbose_name = "Tipo de Servicio"
        verbose_name_plural = "Tipos de Servicio"
        ordering = ('descripcion',)


class ServicioTipoDet(models.Model):
    idService = models.ForeignKey(ServicioCab, verbose_name=varFac, on_delete=models.PROTECT)
    idServiceTipo = models.ForeignKey(ServicioTipo, verbose_name="Servicio aplicado", on_delete=models.PROTECT)

    def __str__(self):
        return '{}'.format(self.idServiceTipo)

    class Meta:
        verbose_name = "Detalle Tipo de Servicio en Factura"
        verbose_name_plural = "Detalles Tipo de Servicios en Facturas"
        ordering = ('idService',)


class ServicioMaquDet(models.Model):
    idService = models.ForeignKey(ServicioCab, verbose_name=varFac, on_delete=models.PROTECT)
    idMaquinaria = models.ForeignKey(Maquinaria, verbose_name="Maquinaria", on_delete=models.PROTECT)

    def __str__(self):
        return '{}'.format(self.idMaquinaria)

    class Meta:
        verbose_name = "Detalle Maquinaria en Factura"
        verbose_name_plural = "Detalles de Maquinarias en Facturas"
        ordering = ('idService',)


class ServicioEquiDet(models.Model):
    idService = models.ForeignKey(ServicioCab, verbose_name=varFac, on_delete=models.PROTECT)
    idEquipo = models.ForeignKey(Equipo, verbose_name="Equipo", on_delete=models.PROTECT)

    def __str__(self):
        return '{}'.format(self.idEquipo)

    class Meta:
        verbose_name = "Detalle Equipo en Factura Servicio"
        verbose_name_plural = "Detalles Equipos en Facturas"
        ordering = ('idService',)


class ServicioProdDet(models.Model):
    idService = models.ForeignKey(ServicioCab, verbose_name=varFac, on_delete=models.PROTECT)
    idProducto = models.ForeignKey(Producto, verbose_name="Producto", on_delete=models.PROTECT)
    cantidad = models.DecimalField("Cantidad", default=1, max_digits=4, decimal_places=0)

    def __str__(self):
        return '{}'.format(self.idProducto)

    class Meta:
        verbose_name = "Detalle Producto en Factura Servicio"
        verbose_name_plural = "Detalles Producto en Facturas"
        ordering = ('idService',)


class ServicioTrabDet(models.Model):
    idService = models.ForeignKey(ServicioCab, verbose_name=varFac, on_delete=models.PROTECT)
    cedulaEmp = models.ForeignKey(Empleado, verbose_name="Empleado", on_delete=models.PROTECT)

    def __str__(self):
        return '{}'.format(self.cedulaEmp)

    class Meta:
        verbose_name = "Detalle Trabajador en Factura Servicio"
        verbose_name_plural = "Detalles Trabajador en Facturas"
        ordering = ('idService',)


class ServicioDomicilio(models.Model):
    idService = models.ForeignKey(ServicioCab, verbose_name=varFac, on_delete=models.PROTECT)
    idTranspor = models.ForeignKey(TransportadorCualificado, verbose_name="Transportador", on_delete=models.PROTECT)
    horaRecogida = models.DateTimeField(auto_now=False)
    tarifa = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return '{} - (${})'.format(self.idTranspor, self.tarifa)

    class Meta:
        verbose_name = "Detalle Transportador en Factura Servicio"
        verbose_name_plural = "Detalles Transportadores en Facturas"
        ordering = ('idService',)


class ServicioCalificacion(models.Model):
    idService = models.ForeignKey(ServicioCab, verbose_name=varFac, on_delete=models.PROTECT)
    cedulaCliente = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.PROTECT)
    calificacion = models.DecimalField("Calificación", default=0, max_digits=1, decimal_places=0)
    opinion = models.TextField("Opinión", max_length="150", default="Sin opinión")

    def __str__(self):
        return '{} - {}/5'.format(self.cedulaCliente, self.calificacion)

    class Meta:
        verbose_name = "Calificación de Servicio"
        verbose_name_plural = "Calificaciones de Servicios"
        ordering = ('idService',)
