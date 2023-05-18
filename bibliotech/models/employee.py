from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    file_number = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
