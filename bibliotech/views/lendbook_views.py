from django.shortcuts import render, redirect
from ..models.lendbook import LendBook
from ..forms.lendbook_form import LendBookForm


def lendbook_list(request):
    lendbooks = LendBook.objects.all()
    context = {
        "lendbooks": lendbooks,
        "title": "Lista de Prestamos",
    }
    return render(request, "lendbook_list.html", context)


def lendbook_create(request):
    form = LendBookForm()
    context = {
        "form": form,
        "submit": "Crear",
        "title": "Crear Prestamo",
        "action": "btn-primary",
    }
    if request.method == "POST":
        form = LendBookForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "lendbook_form.html", context)
