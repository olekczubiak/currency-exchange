from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .models import Cantor
from .serializers import CantorSerializer

class CantorView(generics.ListAPIView):
    queryset = Cantor.objects.all()
    serializer_class = CantorSerializer

class Last12RecordView(generics.ListAPIView):
    queryset = Cantor.objects.order_by('-id').all()[:12]
    serializer_class = CantorSerializer



