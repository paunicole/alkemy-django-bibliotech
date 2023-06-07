import requests
from django.contrib.staticfiles.storage import staticfiles_storage
from django.db import models
from .author import Author
from django.core.exceptions import ValidationError


def validate_isbn(isbn):
    isbn_str = str(isbn)
    if len(isbn_str) != 13:
        raise ValidationError("El ISBN debe tener 13 dígitos.")

    for digit in isbn_str:
        if not digit.isdigit():
            raise ValidationError("El ISBN debe contener solo dígitos.")

    checksum = 0
    for i, digit in enumerate(isbn_str[:-1]):
        weight = 1 if i % 2 == 0 else 3
        checksum += int(digit) * weight
    expected_checksum = (10 - (checksum % 10)) % 10
    if int(isbn_str[-1]) != expected_checksum:
        raise ValidationError(
            "El ISBN es inválido. Comprueba los dígitos y la suma de verificación."
        )

    prefix = isbn_str[:3]
    if prefix not in ("978", "979"):
        raise ValidationError(
            "El ISBN es inválido. Comprueba el prefijo (debe ser 978 o 979)."
        )

    return isbn


def get_default_cover_image():
    return "https://sciendo.com/_next/image?url=%2Fproduct-not-found.png"


class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    isbn = models.IntegerField(
        unique=True,
        validators=[validate_isbn],
        error_messages={"unique": "Ya existe un libro con este ISBN."},
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_cover_image(self, size="L"):
        url = f"https://covers.openlibrary.org/b/isbn/{self.isbn}-{size}.jpg"

        try:
            response = requests.get(url)
            response.raise_for_status()

            return response.url
        except requests.exceptions.HTTPError:
            return get_default_cover_image()
