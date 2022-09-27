from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from publications.models import Publications
from publications.serializers import PublicationsSerializer


class PublicationsView(viewsets.ModelViewSet):
    queryset = Publications.objects.all()
    serializer_class = PublicationsSerializer
