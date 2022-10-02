from .models import Publications, Template, Category
from rest_framework import serializers

class DynamicPublicationFields(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)    



class PublicationsSerializer(DynamicPublicationFields):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Publications
        fields = serializers.ALL_FIELDS


class TemplateSerialixer(DynamicPublicationFields):
    id = serializers.IntegerField(required=False)
    publication = PublicationsSerializer(fields=("id", "patronim"))
    
    class Meta:
        model = Template
        # fields = ["name", "topic", "publication__name"]
        fields = serializers.ALL_FIELDS    
    
    def create(self, validated_data):
        publication_data = validated_data.pop("publication")
        template = Template.objects.create(publication_id=publication_data["id"], **validated_data)
        return template


class CategorySerializer(serializers.ModelSerializer):
    publication = PublicationsSerializer(fields=("id", "name", "patronim"))
    template = TemplateSerialixer(fields=("id", "topic", "publication"))

    class Meta:
        model = Category
        # fields = ["name", "topic", "publication__name"]
        fields = serializers.ALL_FIELDS

    def create(self, validated_data):
        publication_data = validated_data.pop("publication")
        template_data = validated_data.pop("template")
        category = Category.objects.create(publication_id=publication_data["id"], template_id=template_data["id"], **validated_data)
        return category