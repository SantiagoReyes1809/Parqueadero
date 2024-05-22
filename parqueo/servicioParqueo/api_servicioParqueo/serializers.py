from rest_framework import serializers
from .models import Parqueadero
from .models import Ticket

class ParqueaderoSerializer(serializers.ModelSerializer):
    tarifa_hora = serializers.DecimalField(max_digits=10, decimal_places=2)
    tarifa_hora_currency = serializers.CharField(max_length=3)

    class Meta:
        model = Parqueadero
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
