from django.shortcuts import render, redirect
from ..models.employee import Employee
from ..forms.employee_form import EmployeeForm


def employee_list(request):
    employees = Employee.objects.all()
    context = {"employees": employees}
    return render(request, "employee_list.html", context)


def employee_create(request):
    form = EmployeeForm()
    context = {
        "form": form,
        "submit": "Crear",
        "title": "Crear Empleado",
        "action": "btn-primary",
    }
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee-list")
    return render(request, "employee_form.html", context)


def employee_update(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    form = EmployeeForm(instance=employee)
    context = {
        "form": form,
        "submit": "Modificar",
        "title": "Modificar Empleado",
        "action": "btn-warning",
    }

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee-list")  # redirigir a la lista de empleados

    return render(
        request,
        "employee_form.html",
        context,
    )
