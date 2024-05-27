from django.shortcuts import render, redirect, get_object_or_404
from .forms import TicketForm
from .models import Ticket

def home(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TicketForm()
    
    tickets = Ticket.objects.all()
    return render(request, 'index.html', {'form': form, 'tickets': tickets})

def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.delete()
    return redirect('home')

