from rest_framework import viewsets, permissions
from ..serializers.book_serializer import BookSerializer
from bibliotech.models import Book


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BookSerializer
