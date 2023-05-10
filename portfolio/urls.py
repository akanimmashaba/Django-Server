from django.urls import path, include
from .views import OurWorksListView

urlpatterns = [
    path('', OurWorksListView.as_view(), name='our-works')

] 
