from django.shortcuts import render, redirect, get_object_or_404
from ..models.book import Book
from ..forms.book_form import BookForm


def book_list(request):
    books = Book.objects.all()
    context = {
        "books": books,
        "title": "Lista de Libros",
    }
    return render(request, "book_list.html", context)


def book_create(request):
    form = BookForm()
    context = {
        "form": form,
        "submit": "Crear",
        "title": "Crear Libro",
        "action": "btn-primary",
    }
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book-list")
    return render(request, "book_form.html", context)


def book_update(request, book_id):
    book = Book.objects.get(id=book_id)
    form = BookForm(instance=book)
    context = {
        "form": form,
        "submit": "Modificar",
        "title": "Modificar Libro",
        "action": "btn-warning",
    }

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book-list")

    return render(
        request,
        "book_form.html",
        context,
    )


def book_disable(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.is_active = False
    book.save()
    return redirect("book-list")


def book_enable(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.is_active = True
    book.save()
    return redirect("book-list")
