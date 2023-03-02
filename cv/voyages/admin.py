from django.contrib import admin

# Register your models here.
from .models import Voyage, Event, Vehicle, Stay, Voyager

admin.site.register(Voyage)
admin.site.register(Event)
admin.site.register(Vehicle)
admin.site.register(Stay)
admin.site.register(Voyager)
