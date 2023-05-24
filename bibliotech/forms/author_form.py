from ..models.author import Author
from django import forms
from django_countries.widgets import CountrySelectWidget


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "nationality", "is_active"]
        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido",
            "nationality": "Nacionalidad",
            "is_active": "Activo",
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "nationality": CountrySelectWidget(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(),
        }
