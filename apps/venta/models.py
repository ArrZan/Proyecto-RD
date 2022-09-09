from django.db import models
from apps.cliente.models import Cliente
from apps.personal.models import Empleado
from apps.Activos.models import Producto


class FormaPago(models.Model):
    forma = models.CharField("Forma de Pago", max_length=25, unique=True)

    def __str__(self):
        return '{}'.format(self.forma)

    class Meta:
        verbose_name = "Forma de Pago"
        verbose_name_plural = "Formas de Pagos"
        ordering = ('forma',)


class VentaCab(models.Model):
    cedulaCliente = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.PROTECT)
    cedulaEmpleado = models.ForeignKey(Empleado, verbose_name="Empleado", on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    idFormaPago = models.ForeignKey(FormaPago, verbose_name="Forma de Pago", on_delete=models.PROTECT)
    precioTotal = models.DecimalField("Total a Pagar", default=0, max_digits=10, decimal_places=2)
    cambio = models.DecimalField("Cambio", default=0, max_digits=10, decimal_places=2)


    def __str__(self):
        return '{0} {1} - {2} (${3})'.format(self.id, self.fecha.datetime.date(), self.cedulaCliente, self.precioTotal)

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ('fecha',)


class VentaDet(models.Model):
    idVentaCab = models.ForeignKey(VentaCab, verbose_name="Factura", on_delete=models.PROTECT)
    idProducto = models.ForeignKey(Producto, verbose_name="Producto", on_delete=models.PROTECT)
    cantidad = models.DecimalField("Cantidad", default=0, max_digits=4, decimal_places=0)
    precio = models.DecimalField("Precio", default=0, max_digits=6, decimal_places=2)
    monto = models.DecimalField("Monto", default=0, max_digits=6, decimal_places=2)

    def __str__(self):
        return {'{} - {}'.format(self.idProducto, self.cantidad)}

    class Meta:
        verbose_name = "Detalle de Factura"
        verbose_name_plural = "Detalles de Facturas"
        ordering= ('idVentaCab',)