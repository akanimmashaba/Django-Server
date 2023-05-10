from django.urls import path, include
from .views import ClientListView,index

urlpatterns = [
    path('', index, name='index'),
    path('/our-clients', ClientListView.as_view(), name='our-clients'),
    path('/services', include('services.urls') ),
    path('/contact', include('accounts.urls') ),
    path('/our-works', include('portfolio.urls') ),
    path('/tinymce', include('tinymce.urls')),
] 
