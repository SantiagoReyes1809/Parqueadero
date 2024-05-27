from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['placa_vehiculo', 'hora_ingreso', 'propietario_vehiculo']
