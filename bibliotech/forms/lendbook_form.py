from ..models.member import Member
from ..models.book import Book
from ..models.employee import Employee
from ..models.lendbook import LendBook
from django import forms
from datetime import datetime, timedelta


class LendBookForm(forms.ModelForm):
    member = forms.ModelChoiceField(
        queryset=Member.objects.all(),
        empty_label="Seleccione un miembro",
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        ),
    )
    book = forms.ModelChoiceField(
        queryset=Book.objects.all(),
        empty_label="Seleccione un libro",
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        ),
    )
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        empty_label="Seleccione un empleado",
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = datetime.now()
        self.fields["lend_date"].initial = today
        self.fields["return_date"].initial = today + timedelta(days=2)

    class Meta:
        model = LendBook
        fields = ["member", "book", "employee", "lend_date", "return_date"]
        labels = {
            "member": "Miembro",
            "book": "Libro",
            "employee": "Empleado",
            "lend_date": "Fecha de préstamo",
            "return_date": "Fecha de devolución",
        }
        widgets = {
            "member": forms.Select(
                attrs={"class": "form-control", "placeholder": "Miembro"}
            ),
            "book": forms.Select(
                attrs={"class": "form-control", "placeholder": "Libro"}
            ),
            "employee": forms.Select(
                attrs={"class": "form-control", "placeholder": "Empleado"}
            ),
            "lend_date": forms.DateTimeInput(
                format="%Y-%m-%d",
                attrs={
                    "class": "form-control",
                    "placeholder": "Fecha de préstamo",
                    "readonly": True,
                },
            ),
            "return_date": forms.DateTimeInput(
                format="%Y-%m-%d",
                attrs={
                    "class": "form-control",
                    "placeholder": "Fecha de devolución",
                    "readonly": True,
                },
            ),
        }
