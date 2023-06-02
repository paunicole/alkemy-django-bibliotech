from django.shortcuts import render, redirect, get_object_or_404
from ..models.member import Member
from ..forms.member_form import MemberForm


def member_create(request):
    form = MemberForm()
    context = {
        "form": form,
        "submit": "Crear",
        "title": "Crear Socio",
        "action": "btn-primary",
    }
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("member-list")
    return render(request, "member_form.html", context)


def member_update(request, member_id):
    member = Member.objects.get(id=member_id)
    form = MemberForm(instance=member)
    context = {
        "form": form,
        "submit": "Modificar",
        "title": "Modificar Socio",
        "action": "btn-warning",
    }

    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect("member-list")

    return render(
        request,
        "member_form.html",
        context,
    )


def member_disable(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.is_active = False
    member.save()
    return redirect("member-list")


def member_enable(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.is_active = True
    member.save()
    return redirect("member-list")
