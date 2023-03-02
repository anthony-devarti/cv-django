from django.db import models

# Create your models here.
class Voyage(models.Model):
    name = models.CharField(max_length=200)
    ###Date time fields are dumb
    departure = models.CharField(max_length=200)
    return_date = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    event_date = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    mtg_format = models.CharField(max_length=200)
    entry = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    def __str__(self):
        return self.name

# Voyager is an extension of user, so as to not interfere with django's built-in users
class Voyager(models.Model):
    display_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return self.display_name

class Vehicle(models.Model):
    public_name = models.CharField(max_length=200)
    private_name = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    mileage = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    license_plate_number = models.CharField(max_length=200)
    seats = models.CharField(max_length=200)
    trunk_available = models.CharField(max_length=200)
    smoking = models.CharField(max_length=200)
    owner = models.ForeignKey(Voyager, on_delete=models.CASCADE)
    def __str__(self):
        return self.license_plate_number

class Stay(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    