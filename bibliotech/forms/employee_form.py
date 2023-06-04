from ..models.employee import Employee
from django import forms


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["first_name", "last_name", "file_number"]
        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido",
            "file_number": "Número de legajo",
        }

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Apellido"}
            ),
            "file_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Número de legajo",
                    "disabled": True,
                }
            ),
        }
