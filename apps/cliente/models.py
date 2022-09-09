from django.db import models

class Cliente(models.Model):
    cedulaCliente = models.CharField("Cédula", max_length=10, primary_key=True, unique=True)
    nombres = models.CharField("Nombres", max_length=40)
    apellidos = models.CharField("Apellidos", max_length=40)
    telefono = models.CharField("Teléfono", max_length=10, unique=True)
    correo = models.EmailField("Correo", max_length=50, unique=True)
    direccion = models.TextField("Dirección", blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ('nombres','-apellidos')


class VehiculoMarca(models.Model):
    marca = models.CharField("Marca de Vehículo", max_length=35, unique=True)

    def __str__(self):
        return '{}'.format(self.marca)

    class Meta:
        verbose_name = "Marca de Vehículo"
        verbose_name_plural = "Marcas de Vehículos"
        ordering = ('marca',)


class VehiculoModelo(models.Model):
    modelo = models.CharField("Modelo de Vehículo", max_length=35, unique=True)
    idMarca = models.ForeignKey(VehiculoMarca, verbose_name="Marca de Vehículo", on_delete=models.PROTECT)

    def __str__(self):
        return '{}'.format(self.modelo)

    class Meta:
        verbose_name = "Modelo de Vehículo"
        verbose_name_plural = "Modelos de Vehículos"
        ordering = ('modelo',)

class VehiculoCarroceria(models.Model):
    nombre = models.CharField("Carrocería de Vehículo", max_length=30, unique=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name = "Carrocería de Vehículo"
        verbose_name_plural = "Carrocerías de Vehículos"
        ordering = ('nombre',)


class Vehiculo(models.Model):
    añoFabri = models.DateField("Año de Fabricación")
    placa = models.CharField("Placa", max_length=10, unique=True)
    idCarroceria = models.ForeignKey(VehiculoCarroceria, verbose_name="Carrocería", on_delete=models.PROTECT)
    cedulaCli = models.ForeignKey(Cliente, verbose_name="Propietario", on_delete=models.CASCADE)
    idModelo = models.ForeignKey(VehiculoModelo, verbose_name="Modelo vehicular", on_delete=models.PROTECT)

    def __str__(self):
        return '{0} - ({1})'.format(self.idCarroceria, self.placa)

    class Meta:
        verbose_name="Vehículo"
        verbose_name_plural="Vehículos"
        ordering=('idCarroceria',)