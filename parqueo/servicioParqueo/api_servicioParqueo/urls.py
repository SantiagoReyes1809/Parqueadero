from django.urls import path
from . import views
from .views import * 

urlpatterns = [
    path ('', views.home, name='home'),
    path('parqueadero', ParqueaderoViewSet.as_view()),
    path('ticket', TicketViewSet.as_view()),
    path('front', MyFrontendView.as_view()),
]