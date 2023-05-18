from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
