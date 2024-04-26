from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('list_vehicles/', views.list_vehicles, name='list_vehicles'),
    path('vehicles_info/<int:pk>/', views.vehicle_info, name='vehicles_info')
]
