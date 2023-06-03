from ..models.book import Book
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description", "isbn", "author"]
        labels = {
            "title": "Título",
            "description": "Descripción",
            "isbn": "ISBN",
            "author": "Autor",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Título"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Descripción"}
            ),
            "isbn": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "ISBN"}
            ),
            "author": forms.Select(
                attrs={"class": "form-control", "placeholder": "Autor"}
            ),
        }
