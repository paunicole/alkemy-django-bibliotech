from rest_framework import serializers
from bibliotech.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "first_name", "last_name", "file_number", "is_active"]
