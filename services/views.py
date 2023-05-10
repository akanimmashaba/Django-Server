# Create your views here.
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Service


class ServicesListView(ListView):
    template_name = 'services.html'  # Specify your own template name/location
    model = Service
    queryset = Service.objects.all()[:4]

