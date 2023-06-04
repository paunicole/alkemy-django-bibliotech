from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    file_number = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def format_file_number(self):
        return str(self.file_number).zfill(8)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
