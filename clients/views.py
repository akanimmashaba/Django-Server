from django.shortcuts import render
from django.views.generic import ListView
from services.models import Service
from .models import Client



# Create your views here.
class ClientListView(ListView):
    pass

def index(request):
    services = Service.objects.all()
    clients = Client.objects.all()
    context = {
        'services': services,
        'clients': clients,
    }
    return render(request, 'index.html', context)
