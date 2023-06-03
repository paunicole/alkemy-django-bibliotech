from ..models.author import Author
from django import forms
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField


class AuthorForm(forms.ModelForm):
    nationality = CountryField(blank_label="Seleccione un país").formfield(
        widget=CountrySelectWidget(attrs={"class": "form-control"})
    )

    class Meta:
        model = Author
        fields = ["first_name", "last_name", "nationality"]
        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido",
            "nationality": "Nacionalidad",
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Apellido"}
            ),
        }
