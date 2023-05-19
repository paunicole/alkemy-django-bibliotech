from django.db import models
from .author import Author
from django.core.exceptions import ValidationError


def validate_isbn(isbn):
    if len(str(isbn)) != 13:
        raise ValidationError("Número de ISBN inválido.")


class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    isbn = models.IntegerField(unique=True, validators=[validate_isbn])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
