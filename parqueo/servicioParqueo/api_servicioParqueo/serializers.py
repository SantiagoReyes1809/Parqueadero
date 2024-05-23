from rest_framework import serializers, viewsets, generics
from rest_framework.response import Response
from .models import Parqueadero, Ticket

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

class TicketByPropietarioViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer

    def get_queryset(self):
        propietario = self.request.query_params.get('propietario', None)
        if propietario is not None:
            queryset = Ticket.objects.filter(propietario_vehiculo=propietario)
        else:
            queryset = Ticket.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

