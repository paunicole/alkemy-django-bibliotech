from rest_framework import serializers
from bibliotech.models import Author
from django_countries.serializer_fields import CountryField


class AuthorSerializer(serializers.ModelSerializer):
    nationality = CountryField()

    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name", "nationality", "is_active"]

    def get_nationality(self, obj):
        return obj.nationality.name if obj.nationality else None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["nationality"] = self.get_nationality(instance)
        return representation
