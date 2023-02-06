from django.shortcuts import render
from clients.models import Clients
from clients.forms import ClientForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView,ListView,UpdateView,DeleteView
# Create your views here.

class ClientCreateView(CreateView):
    model = Clients
    template_name = 'Clientes/create_client.html'
    fields = '__all__'
    success_url = '/clients/list_clients/'

class ClientListView(LoginRequiredMixin,ListView):
    model = Clients
    template_name = 'Clientes/list_clients.html'


class ClientUpdateView(UpdateView):
    model = Clients
    template_name = 'Clientes/update_client.html'
    fields = '__all__'
    success_url = '/clients/list_clients/'

class ClientDeleteView(DeleteView):
    model = Clients
    template_name= 'Clientes/delete_client.html'
    success_url= '/clients/list_clients/'

