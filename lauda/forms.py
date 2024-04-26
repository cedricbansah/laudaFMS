from django import forms
from .models import Vehicle, User
from django_registration.forms import RegistrationForm


# class CreateVehicleForm(forms.ModelForm):
#     # Form for creating a new vehicle
#
#     class Meta:
#         model = Vehicle
#         fields = ['year',
#                   'make',
#                   'model',
#                   'color',
#                   'license_plate',
#                   'vehicle_type',
#                   ]
#

class UserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User
