from django.db import models


class Vehicle(models.Model):
    # Model to represent a vehicle
    HATCHBACK = "Hatchback"
    SEDAN = "Sedan"
    SUV = "SUV"
    MINIVAN = "Minivan"
    PICK_UP = "Pick-Up Truck"
    VEHICLE_TYPES = (
        (HATCHBACK, "Hatchback"),
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (MINIVAN, "Minivan"),
        (PICK_UP, "Pick-Up Truck")
    )

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    STATUS_OPTIONS = (
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive")
    )

    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField
    registration_number = models.CharField(max_length=255, unique=True)
    color = models.CharField(max_length=255)

    vehicle_type = models.CharField(
        max_length=255,
        choices=VEHICLE_TYPES
    )

    vehicle_status = models.CharField(
        max_length=10,
        choices=STATUS_OPTIONS,
        default=ACTIVE
    )

    #    driver_assigned = models.ForeignKey(Driver, to_field=registration_number, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {self.license_plate}"


class Driver(models.Model):
    # Model to represent a driver
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField
    email = models.EmailField
    phone_number = models.CharField(max_length=10)
    license_number = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    vehicle_assigned = models.ForeignKey(Vehicle.registration_number, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.license_number}"
