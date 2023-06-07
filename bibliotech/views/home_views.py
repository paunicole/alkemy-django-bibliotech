from django.shortcuts import render
from ..models.book import Book


def front_home(request):
    books = Book.objects.all()
    context = {
        "books": books,
        "title": "Lista de Libros",
    }
    return render(request, "home.html", context)
