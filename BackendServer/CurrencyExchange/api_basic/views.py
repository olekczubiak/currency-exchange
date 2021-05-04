from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .models import Cantor
from .serializers import CantorSerializer

class CantorView(generics.CreateAPIView):
    queryset = Cantor.objects.all()
    serializer_class = CantorSerializer


