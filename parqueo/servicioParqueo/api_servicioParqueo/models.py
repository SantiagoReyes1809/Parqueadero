from django.db import models

class Parqueadero(models.Model):
    nombre = models.CharField(max_length=255)
    tarifa_hora = models.DecimalField(max_digits=10, decimal_places=2)
    tarifa_hora_currency = models.CharField(max_length=3, default='COP')
    hora_apertura = models.TimeField()
    hora_cierre = models.TimeField()

class Ticket(models.Model):
    parqueadero = models.ForeignKey(Parqueadero, on_delete=models.CASCADE)
    placa_vehiculo = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=True, blank=True)
