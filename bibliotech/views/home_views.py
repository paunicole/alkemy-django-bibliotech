from django.shortcuts import render
from ..models.book import Book


def front_home(request):
    books = Book.objects.all()
    context = {
        "books": books,
        "title": "Lista de Libros",
    }
    for book in books:
        book.image_path = book.get_cover_image()

    return render(request, "home.html", context)
