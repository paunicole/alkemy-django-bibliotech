from django.db import models
from datetime import date
from django.core.exceptions import ValidationError


def validate_birth_date(value):
    if value > date.today():
        raise ValidationError("La fecha de nacimiento no puede ser en el futuro.")

    year = value.year

    max_age = 120
    if date.today().year - year > max_age:
        raise ValidationError("Fecha de nacimiento inválida. La edad máxima es 120.")

    min_age = 10
    if date.today().year - year < min_age:
        raise ValidationError(
            "Fecha de nacimiento inválida. Debe ser mayor de 10 años para registrarse."
        )


class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(validators=[validate_birth_date])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
