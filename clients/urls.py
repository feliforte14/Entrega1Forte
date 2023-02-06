from django.urls import path
from clients.views import ClientCreateView,ClientListView,ClientUpdateView,ClientDeleteView
urlpatterns = [
    path('list_clients/',ClientListView.as_view()),
    path('create_client/',ClientCreateView.as_view()),
    path('update_client/<int:pk>',ClientUpdateView.as_view()),
    path('delete_client/<int:pk>',ClientDeleteView.as_view()),

]