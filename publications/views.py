from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from publications.models import Publications, Template, Category
from publications.serializers import PublicationsSerializer, TemplateSerialixer, CategorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class PublicationsView(viewsets.ModelViewSet):
    queryset = Publications.objects.all()
    serializer_class = PublicationsSerializer

    @action(detail=False, methods=['get'])  
    def kek(self, request):
        gf = "gdhd"
        return Response("Че за 3")

class TemplateView(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerialixer 


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 