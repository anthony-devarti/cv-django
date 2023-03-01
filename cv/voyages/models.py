from django.db import models

# Create your models here.
class Voyage(models.Model):
    name = models.CharField(max_length=200)
    ###Date time fields are dumb
    departure = models.CharField(max_length=200)
    return_date = models.CharField(max_length=200)

class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    event_date = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    mtg_format = models.CharField(max_length=200)
    entry = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)