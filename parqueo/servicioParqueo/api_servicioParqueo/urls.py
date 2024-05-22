from django.urls import path
from .views import * 

urlpatterns = [

    path('parqueadero', ParqueaderoViewSet.as_view()),
    path('ticket', TicketViewSet.as_view()),
    path('front', MyFrontendView.as_view()),
]