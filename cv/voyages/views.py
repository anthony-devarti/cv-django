from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Vehicle
from rest_framework import viewsets
from rest_framework import permissions
from voyages.serializers import *
from django.contrib.auth.models import User, Group

def index(request):
    return HttpResponse("Hello, world. You're at the voyages index.")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows vehicles to be viewed or edited.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.AllowAny]

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]

class VoyagerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Voyager.objects.all()
    serializer_class = VoyagerSerializer
    permission_classes = [permissions.AllowAny]

class StayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stays to be viewed or edited.
    """
    queryset = Stay.objects.all()
    serializer_class = StaySerializer
    permission_classes = [permissions.AllowAny]