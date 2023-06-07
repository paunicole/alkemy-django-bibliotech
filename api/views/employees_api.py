from django.http import JsonResponse
from bibliotech.models.employee import Employee


def employee_list(request):
    employees = Employee.objects.all()
    employees_list = []
    for employee in employees:
        employees_list.append(
            {
                "id": employee.id,
                "first_name": employee.first_name,
                "last_name": employee.last_name,
                "file_number": employee.file_number,
                "is_active": employee.is_active,
            }
        )
    return JsonResponse({"employees": employees_list})


def employee_id(request, pk):
    employee = Employee.objects.get(id=pk)
    employee_detail = {
        "id": employee.id,
        "first_name": employee.first_name,
        "last_name": employee.last_name,
        "file_number": employee.file_number,
        "is_active": employee.is_active,
    }
    return JsonResponse({"employee": employee_detail})
