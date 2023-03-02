from django.contrib.auth.models import User, Group
from rest_framework import serializers
from voyages.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'first_name', 'last_name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields= ['id', 'public_name', 'private_name', 'license_plate_number', 'mileage', 'year', 'make', 'model']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'location', 'event_date', 'start_time', 'mtg_format', 'entry', 'qualification']

class VoyagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voyager
        fields = ['id', 'first_name', 'last_name']

class StaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stay
        fields = ['id', 'name', 'address', 'start_date', 'end_date']