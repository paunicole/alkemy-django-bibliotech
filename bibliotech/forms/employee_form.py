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
                    "readonly": True,
                }
            ),
        }

    def save(self, commit=True):
        if self.instance.pk:
            self.fields.pop("file_number")
        return super().save(commit=commit)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if Employee.objects.exists():
            last_file_number = Employee.objects.last().file_number
        else:
            last_file_number = 0
        next_file_number = str(last_file_number + 1).zfill(8)
        self.fields["file_number"].initial = next_file_number
