from dataclasses import fields
from django.db import models
from drf_writable_nested.mixins import UniqueFieldsMixin, NestedUpdateMixin
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

# Create your models here.

class Child(models.Model):
    field = models.CharField(max_length=100, unique=True)


class Parent(models.Model):
    child = models.ForeignKey('Child', on_delete=models.CASCADE)




class ChildSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = serializers.ALL_FIELDS


class ParentSerializer(WritableNestedModelSerializer):
    child = ChildSerializer()

    class Meta:
        model = Parent
        fields = serializers.ALL_FIELDS
