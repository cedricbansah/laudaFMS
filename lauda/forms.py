from django import forms
from .models import Vehicle

class CreateVehicleForm(forms.ModelForm):
    # Form for creating a new vehicle

    class Meta:
        model = Vehicle
        fields = ['year',
                  'make',
                  'model',
                  'color',
                  'license_plate',
                  'vehicle_type',
                  ]
