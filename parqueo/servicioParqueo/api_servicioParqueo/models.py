from django.db import models

class Parqueadero(models.Model):
    nombre = models.CharField(max_length=255)
    tarifa_hora = models.DecimalField(max_digits=10, decimal_places=2)
    tarifa_hora_currency = models.CharField(max_length=3, default='COP')
    hora_apertura = models.TimeField()
    hora_cierre = models.TimeField()

class Ticket(models.Model):
    placa_vehiculo = models.CharField(max_length=20)
    hora_ingreso = models.DateTimeField()
    propietario_vehiculo = models.CharField(max_length=255)

    def __str__(self):
        return f"Ticket de entrada: {self.placa_vehiculo} - Propietario: {self.propietario_vehiculo}"

