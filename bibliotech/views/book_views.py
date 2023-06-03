from django.shortcuts import render, redirect
from ..forms.book_form import BookForm


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
