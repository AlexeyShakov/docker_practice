from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from publications.models import Publications
from publications.serializers import PublicationsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import debugpy
import seaborn

class PublicationsView(viewsets.ModelViewSet):
    queryset = Publications.objects.all()
    serializer_class = PublicationsSerializer

    @action(detail=False, methods=['get'])  
    def kek(self, request):
        gf = "gdhd"
        return Response("Че за dada")