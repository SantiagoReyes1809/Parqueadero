from urllib import response
from django.shortcuts import render
from rest_framework import  permissions
from .models import Parqueadero, Ticket
from .serializers import ParqueaderoSerializer, TicketSerializer
from .models import Parqueadero
from django.views.generic import TemplateView
from rest_framework.views import APIView


def home(request):
    return render(request, 'index.html')

class ParqueaderoViewSet(APIView):
    queryset = Parqueadero.objects.all()
    serializer_class = ParqueaderoSerializer
    permission_classes = [permissions.AllowAny]

class TicketViewSet(APIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, request, *args, **kwargs):
        ticket = self.get_object()

        if not ticket.fecha_salida:
            ticket.fecha_salida = request.data.POST('fecha_salida')
            ticket.save()

            tiempo_estacionado = ticket.fecha_salida - ticket.fecha_ingreso
            horas_estacionadas = tiempo_estacionado.total_seconds() / 3600


            if ticket.parqueadero.tarifa_hora_currency != 'COP':
                tarifa_hora_cop = convert_currency(ticket.parqueadero.tarifa_hora, ticket.parqueadero.tarifa_hora_currency, 'COP')
            else:
                tarifa_hora_cop = ticket.parqueadero.tarifa_hora

            precio_total = horas_estacionadas * tarifa_hora_cop

            response_data = {
                'tiempo_estacionado': horas_estacionadas,
                'precio_total': precio_total,
                'precio_total_currency': 'COP'  
            }

            return response(response_data)

        return super().update(request, *args, **kwargs)
        
class MyFrontendView(TemplateView):
    template_name = "index.html"


