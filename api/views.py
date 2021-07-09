from django.shortcuts import render
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from .models import DataMap
from .serializers import DataMapSer


def search(request):
    return render(request, 'index.html')


class DataMapView(ModelViewSet):
    queryset = DataMap.objects.all()
    serializer_class = DataMapSer
