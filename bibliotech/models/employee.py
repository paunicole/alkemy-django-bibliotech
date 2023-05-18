from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    file_number = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
