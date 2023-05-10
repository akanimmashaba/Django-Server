from django.contrib import admin
from .models import Client
from .models import Company
# Register your models here.


admin.site.register(Company)

admin.site.register(Client)