from ..models.member import Member
from django import forms


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
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "birth_date": forms.DateInput(attrs={"class": "form-control"}),
        }
