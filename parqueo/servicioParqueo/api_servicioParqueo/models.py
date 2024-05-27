from django.db import models

class Ticket(models.Model):
    placa_vehiculo = models.CharField(max_length=20)
    hora_ingreso = models.DateTimeField(null=True, blank=True)
    propietario_vehiculo = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.placa_vehiculo

