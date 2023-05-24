from django.shortcuts import render, redirect
from ..models.employee import Employee
from ..forms.employee_form import EmployeeForm


def employee_list(request):
    employees = Employee.objects.all()
    context = {"employees": employees}
    return render(request, "employee_list.html", context)


def employee_form(request):
    form = EmployeeForm()
    context = {"form": form}
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee-list")
    return render(request, "employee_form.html", context)
