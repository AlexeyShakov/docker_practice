from django.shortcuts import render
from .models import Child, Parent, ChildSerializer, ParentSerializer
from rest_framework import viewsets

# Create your views here.

class ChildView(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class ParentView(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
