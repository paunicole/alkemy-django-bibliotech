from rest_framework import serializers
from bibliotech.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "description", "isbn", "author", "is_active"]
