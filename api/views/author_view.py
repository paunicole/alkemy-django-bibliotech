from rest_framework import viewsets, permissions
from ..serializers.author_serializer import AuthorSerializer
from bibliotech.models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorSerializer
