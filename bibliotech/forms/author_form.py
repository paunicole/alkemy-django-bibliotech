from ..models.author import Author
from django import forms
from django_countries.widgets import CountrySelectWidget


class AuthorForm(forms.ModelForm):
    nationality = CountryField(blank_label="Selecciona un país").formfield(
        widget=CountrySelectWidget(attrs={"class": "form-control"})

      
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "nationality"]
        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido",
            "nationality": "Nacionalidad",
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "nationality": CountrySelectWidget(attrs={"class": "form-control"}),
        }
