from ..models.member import Member
from django import forms
from django.forms.widgets import DateInput


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["first_name", "last_name", "birth_date"]
        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido",
            "birth_date": "Fecha de Nacimiento",
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Apellido"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Apellido"}
            ),
            "birth_date": DateInput(
                format="%Y-%m-%d", attrs={"type": "date", "class": "form-control"}
            ),
        }
