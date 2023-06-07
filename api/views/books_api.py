from django.http import JsonResponse
from bibliotech.models import Book


def book_list(request):
    books = Book.objects.all()
    books_list = []
    for book in books:
        books_list.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description,
                "author": book.author.first_name + " " + book.author.last_name,
                "author_id": book.author.id,
                "is_active": book.is_active,
            }
        )
    return JsonResponse({"books": books_list})


def book_id(request, pk):
    book = Book.objects.get(id=pk)
    book_detail = {
        "id": book.id,
        "title": book.title,
        "description": book.description,
        "author": book.author.first_name + " " + book.author.last_name,
        "author_id": book.author.id,
        "is_active": book.is_active,
    }
    return JsonResponse({"book": book_detail})
