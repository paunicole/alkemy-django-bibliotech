from django.shortcuts import render, redirect
from ..models.author import Author
from ..forms import AuthorForm


def author_view(request, id):
    author = Author.objects.filter(id=id).first()
    context = {
        "author": author,
    }
    return render(request, "author_view.html", context)


def author_list(request):
    authors = Author.objects.all()
    context = {
        "authors": authors,
    }
    return render(request, "author_list.html", context)


def author_create(request):
    form = AuthorForm()
    context = {
        "form": form,
        "submit": "Crear",
        "title": "Crear Autor",
        "action": "btn-primary",
    }
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("author-list")
    return render(request, "author_form.html", context)
