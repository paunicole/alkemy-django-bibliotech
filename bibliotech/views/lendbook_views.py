from django.shortcuts import render, redirect
from ..models.lendbook import LendBook
from ..forms.lendbook_form import LendBookForm


def lendbook_list(request):
    lendbooks = LendBook.objects.all()
    context = {
        "lendbooks": lendbooks,
        "title": "Lista de Préstamos",
    }
    return render(request, "lendbook_list.html", context)


def lendbook_create(request):
    form = LendBookForm()
    context = {
        "form": form,
        "submit": "Crear",
        "title": "Crear Préstamo",
        "action": "btn-primary",
    }
    if request.method == "POST":
        form = LendBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lendbook-list")
    return render(request, "lendbook_form.html", context)


def lendbook_update(request, lendbook_id):
    lendbook = LendBook.objects.get(id=lendbook_id)
    form = LendBookForm(instance=lendbook)
    context = {
        "form": form,
        "submit": "Modificar",
        "title": "Modificar Préstamo",
        "action": "btn-warning",
    }

    if request.method == "POST":
        form = LendBookForm(request.POST, instance=lendbook)
        if form.is_valid():
            form.save()
            return redirect("lendbook-list")

    return render(
        request,
        "lendbook_form.html",
        context,
    )


def lendbook_delete(request, lendbook_id):
    lendbook = LendBook.objects.get(id=lendbook_id)
    lendbook.delete()
    return redirect("lendbook-list")
