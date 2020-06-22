from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from django.contrib.auth.models import User

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.ClientSerializer