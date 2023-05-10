# Create your views here.
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Portfolio


class OurWorksListView(ListView):
    model = Portfolio
    template_name = 'our-works.html'  # Specify your own template name/location
    


