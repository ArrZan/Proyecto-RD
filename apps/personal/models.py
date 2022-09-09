from django.db import models

class Cargo(models.Model):
    funcion = models.CharField("Función", max_length=35, unique=True)
    sueldo = models.DecimalField("Sueldo", default=0, max_digits=6, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.funcion)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        ordering = ('funcion',)


class Empleado(models.Model):
    cedulaEmp = models.CharField("Cédula", max_length=10, primary_key=True, unique=True)
    nombres = models.CharField("Nombres", max_length=40)
    apellidos = models.CharField("Apellidos", max_length=40)
    telefono = models.CharField("Teléfono", max_length=10, unique=True)
    correo = models.EmailField("Correo", max_length=50, unique=True)
    direccion = models.TextField("Dirección", blank=True, null=True)
    cargo = models.ForeignKey(Cargo, verbose_name="Cargo", on_delete=models.PROTECT)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ('nombres','-apellidos')


class ContratoTipo(models.Model):
    contrato = models.CharField("Tipo de Contrato", max_length=40, unique=True)
    tiempo = models.CharField("Tiempo de Contrato", max_length=35)

    def __str__(self):
        return '{0} - ({1})'.format(self.contrato, self.tiempo)

    class Meta:
        verbose_name = "Tipo de Contrato"
        verbose_name_plural = "Tipos de Contratos"
        ordering = ('contrato',)


class Contratacion(models.Model):
    fechaContrato = models.DateField("Fecha de contrato", auto_now_add=True, auto_now=False)
    fechaInicio = models.DateField(verbose_name="Día de comienzo de actividades laborales", auto_now=False, auto_now_add=False)
    cedulaEmp = models.ForeignKey(Empleado, verbose_name="Nombre", on_delete=models.CASCADE)
    tipoContratacion = models.ForeignKey(ContratoTipo, verbose_name="Tipo de Contrato", on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, verbose_name="Cargo a ejercer", on_delete=models.PROTECT)

    def __str__(self):
        return '{} - {}'.format(self.fechaContrato, self.cedulaEmp)

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"
        ordering = ('fechaContrato',)


class TransportadorCualificado(models.Model):
    DocumentoAvalador = models.FileField("Permiso Institucional Avalador", upload_to='Permisos/')
    Estado = models.BooleanField("Estado", default=True)
    cedulaEmp = models.ForeignKey(Empleado, verbose_name="Cédula de Empleado", on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.cedulaEmp)

    class Meta:
        verbose_name = "Transportador Cualificado"
        verbose_name_plural = "Transportadores Cualificados"