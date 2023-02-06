from django.contrib import admin
from clients.models import Clients
# Register your models here.

@admin.register(Clients)
class ClientsAdmin (admin.ModelAdmin):
    list_display=('nombre','email','tipo')