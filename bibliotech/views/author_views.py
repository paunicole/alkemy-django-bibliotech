from django.shortcuts import render, redirect, get_object_or_404
from ..models.author import Author
from ..forms.author_form import AuthorForm


def author_list(request):
    authors = Author.objects.all()
    context = {
        "authors": authors,
        "title": "Lista de Autores",
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


def author_update(request, author_id):
    author = Author.objects.get(id=author_id)
    form = AuthorForm(instance=author)
    context = {
        "form": form,
        "submit": "Modificar",
        "title": "Modificar Autor",
        "action": "btn-warning",
    }

    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect("author-list")

    return render(
        request,
        "author_form.html",
        context,
    )


def author_disable(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.is_active = False
    author.save()
    return redirect("author-list")


def author_enable(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.is_active = True
    author.save()
    return redirect("author-list")
