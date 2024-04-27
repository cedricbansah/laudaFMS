from django.shortcuts import render
from .models import Vehicle, Driver
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

# def list_vehicles(request):
#     # View function to display all vehicles
#     # Get vehicles from database
#
#     vehicles = Vehicle.objects.all()
#     context = {'vehicles': vehicles}
#
#     return render(request, 'vehicles.html', context)
#
#
# def list_drivers(request):
#     # View function to display all drivers
#     # get drivers from DB
#
#     drivers = Driver.objects.all()
#     context = {'drivers': drivers}
#
#     return render(request, 'drivers.html')
#
#
# def vehicle_info(request, pk):
#     # View function to display vehicle information
#     try:
#         vehicle = Vehicle.objects.get(pk=pk)
#     except Vehicle.DoesNotExist:
#         return render(request, '404.html')
#
#     context = {'vehicle': vehicle}
#     return render(request, 'vehicle_info.html', context)
#
