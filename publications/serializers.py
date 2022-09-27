from .models import Publications
from rest_framework import serializers

class PublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = serializers.ALL_FIELDS