from django.db import models
from apps.Activos.choices import CHOICES_REPONER

class ProductoTipo(models.Model):
    nombre = models.CharField("Tipo de Producto", max_length=55, unique=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name = "Tipo de Producto"
        verbose_name_plural = "Tipo de Productos"
        ordering = ('nombre',)


class Producto(models.Model):
    nombre = models.CharField("Nombre del Producto", max_length=45, unique=True)
    descripcion = models.CharField("Descripción", max_length=150, blank=True)
    precio = models.DecimalField("Precio",default=0, max_digits=9, decimal_places=2)
    stock = models.PositiveSmallIntegerField("Cantidad de Producto")
    idProductoTipo = models.ForeignKey(ProductoTipo, verbose_name="Tipo de Producto", on_delete=models.PROTECT)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ('nombre',)


class EquipoTipo(models.Model):
    nombre = models.CharField("Tipo de Equipo", max_length=45, unique=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name = "Tipo de Equipo"
        verbose_name_plural = "Tipo de Equipos"
        ordering = ('nombre',)


class Equipo(models.Model):
    CHOICES_REPONEREQUIP = [
        ('F', 'EN USO'),
        ('V', 'REPONER'),
    ]
    nombre = models.CharField("Nombre de Equipo", max_length=45, unique=True)
    descripcion = models.CharField("Descripción", max_length=150, blank=True)
    estadoReponer = models.CharField("Estado", max_length=1, choices=CHOICES_REPONEREQUIP, default='F')
    idEquipTipo = models.ForeignKey(EquipoTipo,verbose_name="Tipo de Equipo", on_delete=models.PROTECT)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ('nombre',)


class MaquinariaModelo(models.Model):
    modelo = models.CharField("Tipo de maquinaria", max_length=25)

    def __str__(self):
        return '{}'.format(self.modelo)

    class Meta:
        verbose_name = "Tipo de Maquinaria"
        verbose_name_plural = "Tipo de Maquinarias"
        ordering = ('modelo',)


class Maquinaria(models.Model):
    CHOICES_MANTENIMIENTO = [
        ('F', 'NO REQUIERE MANTENIMIENTO'),
        ('V', 'REQUIERE MANTENIMIENTO'),
    ]

    nombre = models.CharField("Maquinaria", max_length=55, unique=True)
    descripcion = models.CharField("Descripción", max_length=150, blank=True)
    fechaAdquisicion = models.DateField("Fecha de Adquisición", auto_now=False)
    EstadoReponer = models.CharField("Estado", max_length=1, choices=CHOICES_REPONER, default='F')
    EstadoMantenimiento = models.CharField("Estado de Mantenimiento", max_length=1, choices=CHOICES_MANTENIMIENTO, default='F')
    observacion = models.TextField("Observaciones", blank=True)
    idMaquModel = models.ForeignKey(MaquinariaModelo, verbose_name="Tipo de Producto", on_delete=models.PROTECT)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name = "Maquinaria"
        verbose_name_plural = "Máquinas"
        ordering = ('nombre',)
