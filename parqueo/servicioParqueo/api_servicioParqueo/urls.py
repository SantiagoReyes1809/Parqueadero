from django.urls import path
from .views import home, delete_ticket

urlpatterns = [
    path('', home, name='home'),
    path('delete/<int:ticket_id>/', delete_ticket, name='delete_ticket'),
]

