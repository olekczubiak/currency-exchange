from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Cantor
from .serializers import CantorSerializer


def courses(request):
    if request.method == 'GET':
        course = Cantor.objects.all()
        serializer = CantorSerializer(course, many=True)
        return JsonResponse(serializer.data, safe=False)


# Create your views here.
