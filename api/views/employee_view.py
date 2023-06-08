from rest_framework import viewsets, permissions
from ..serializers.employee_serializer import EmployeeSerializer
from bibliotech.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmployeeSerializer
