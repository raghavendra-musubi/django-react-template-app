from .models import Room
from .serializers import RoomSerializer
from django.shortcuts import render
from rest_framework import generics 

# Create your views here.

# API views
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

