from django.shortcuts import render
from rest_framework import generics
from .models import item
from .serializers import itemserializer

# Create your views here.
class itemlistcreateview(generics.ListCreateAPIView):
    queryset = item.objects.all()
    serializer_class = itemserializer

class itemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = item.objects.all()
    serializer_class = itemserializer

