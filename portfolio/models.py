from django.db import models
from clients.models import Client
# Create your models here.

class Portfolio(models.Model):
    client = models.ForeignKey("clients.Client", verbose_name=("Client"), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/', height_field=None, width_field=None, max_length=None)
    desc = models.CharField(max_length=255)
    content = models.TextField()